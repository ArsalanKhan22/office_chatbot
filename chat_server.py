# chat_server.py
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
import os

DB_PATH = "chat.db"

class ChatDatabase:
    """Handles all database operations for the chat application."""

    def __init__(self, db_path: str):
        self.db_path = db_path
        self._ensure_db()

    def _ensure_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                receiver TEXT,
                message TEXT,
                timestamp TEXT,
                read INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    def send_message(self, sender: str, receiver: str, message: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        timestamp = datetime.now().isoformat()
        c.execute('''
            INSERT INTO messages (sender, receiver, message, timestamp, read)
            VALUES (?, ?, ?, ?, 0)
        ''', (sender, receiver, message, timestamp))
        conn.commit()
        conn.close()

    def get_messages(self, sender: str, receiver: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            SELECT sender, receiver, message, timestamp FROM messages
            WHERE (sender=? AND receiver=?) OR (sender=? AND receiver=?)
            ORDER BY timestamp ASC
        ''', (sender, receiver, receiver, sender))
        rows = c.fetchall()
        conn.close()
        return rows

    def get_unread_count(self, sender: str, receiver: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            SELECT COUNT(*) FROM messages
            WHERE sender=? AND receiver=? AND read=0
        ''', (sender, receiver))
        count = c.fetchone()[0]
        conn.close()
        return count

    def mark_messages_as_read(self, sender: str, receiver: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            UPDATE messages SET read=1
            WHERE sender=? AND receiver=? AND read=0
        ''', (sender, receiver))
        conn.commit()
        conn.close()

# Initialize Flask app and DB handler
app = Flask(__name__)
db = ChatDatabase(DB_PATH)

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    db.send_message(data["sender"], data["receiver"], data["message"])
    return jsonify({"status": "ok"})

@app.route("/messages", methods=["GET"])
def get_messages():
    sender = request.args.get("sender")
    receiver = request.args.get("receiver")
    messages = db.get_messages(sender, receiver)
    return jsonify(messages)

@app.route("/has_unread", methods=["GET"])
def has_unread():
    sender = request.args.get("sender")
    receiver = request.args.get("receiver")
    count = db.get_unread_count(sender, receiver)
    return jsonify({"unread": count})

@app.route("/mark_read", methods=["POST"])
def mark_read():
    data = request.json
    db.mark_messages_as_read(data["sender"], data["receiver"])
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

