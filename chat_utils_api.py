# chat_utils_api.py
import requests

class ChatClient:
    """
    ChatClient handles communication between the Streamlit frontend
    and the Flask backend via HTTP.
    """

    def __init__(self, server_url: str):
        self.server = server_url.rstrip("/")

    def send_message(self, sender: str, receiver: str, message: str) -> None:
        requests.post(f"{self.server}/send", json={
            "sender": sender,
            "receiver": receiver,
            "message": message
        })

    def get_conversation(self, user1: str, user2: str):
        response = requests.get(f"{self.server}/messages", params={
            "sender": user1,
            "receiver": user2
        })
        return response.json()

    def has_unread_messages(self, receiver: str, sender: str) -> bool:
        response = requests.get(f"{self.server}/has_unread", params={
            "sender": sender,
            "receiver": receiver
        })
        return response.json().get("unread", 0) > 0

    def mark_as_read(self, receiver: str, sender: str) -> None:
        requests.post(f"{self.server}/mark_read", json={
            "sender": sender,
            "receiver": receiver
        })

