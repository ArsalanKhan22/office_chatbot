# 🗨️ Office Chatbot (LAN-based)

A lightweight, real-time office chat application built with **Streamlit**, **Flask**, and **SQLite**, designed for local (LAN) use without the internet.

---

## ✨ Features

- 🔁 Real-time chat with auto-refresh (via `streamlit-autorefresh`)
- 🔔 Notification and audio alert for new messages
- 📦 Lightweight and fast using `Flask` + `SQLite`
- 🔐 Class-based modular design for easy maintenance
- 🌐 Designed for LAN (no cloud server needed)

---

## 📂 Project Structure
```bash
office_chatbot/
├── app.py # Streamlit UI
├── chat_utils_api.py # Streamlit ↔ Flask communication (API client)
├── chat_server.py # Flask server (SQLite backend)
├── assets/
│ └── beep.mp3 # Notification sound
└── requirements.txt # Dependencies

```
---

## 🚀 Getting Started

### 1. ✅ Requirements

- Python 3.7+
- pip

### 2. 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

#### Contents of requirements.txt:
```bash
streamlit==1.35.0
streamlit-autorefresh
flask
requests
```

## 🖥️ Usage
### 🖧 1. Run the Chat Server (on one PC)
```bash
python3 chat_server.py
```
The Flask server will start on:
```bash
http://<server_ip>:8000
```
Replace <server_ip> in chat_utils_api.py with your actual LAN IP address.
Note: Make a directory namely assets and copy beep.mp3 file to that directory.

## 💬 2. Run Streamlit Chat UI (on any PC in the network)

streamlit run app.py

    Each user logs in with their name and selects a recipient to chat with.

## 🧠 Developer Notes

    SQLite is used as the local database on the server PC

    Flask serves API endpoints for sending and receiving messages

    Streamlit is used for user interface (client side)

    Audio notifications play when unread messages are detected

## 🔐 Security (Optional Enhancements)

    🔑 Add authentication per user

    🧾 Use SQLAlchemy or ORM for DB management

    📡 Deploy with gunicorn, nginx, or Docker

    🔐 Add HTTPS with self-signed certs for LAN

## 📜 License

This project is open-source and available under the MIT License.
Feel free to use, modify, and share.

## 🙋‍♂️ Contributions

Pull requests are welcome! Please open an issue first if you want to propose major changes.

## 👨‍💻 Author

Developed by Arsalan Khan
© 2025 – All rights reserved.
