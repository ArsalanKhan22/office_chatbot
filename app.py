# app.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from chat_utils_api import ChatClient

# Configure the Streamlit app
st.set_page_config("📠 Office Chatbot", layout="centered")
st_autorefresh(interval=3000, key="chat_refresh")

# Initialize the chat client
client = ChatClient(server_url="http://localhost:8000")  # Replace with actual server IP if needed

# Sidebar login
st.sidebar.title("👤 Login")
username = st.sidebar.text_input("Your Name", value="Arsalan")

# Available users (can be dynamic in real-world apps)
all_users = ["Awais", "Ali", "Mustafa", "Iftikhar", "Arsalan"]
chat_users = [u for u in all_users if u != username]
receiver = st.sidebar.selectbox("Chat with", chat_users)

if username and receiver:
    st.title(f"💬 Chat: {username} ↔ {receiver}")

    # Notification if new message
    if client.has_unread_messages(username, receiver):
        st.sidebar.markdown(f"🔔 **New message from {receiver}!**")
        st.audio("assets/beep.mp3", format="audio/mp3")

    # Show conversation
    st.markdown("### 📜 Chat History")
    conversation = client.get_conversation(username, receiver)
    for msg in conversation[-20:]:
        sender, _, message, timestamp = msg
        sender_label = "🟢 You" if sender == username else f"🔸 {sender}"
        st.markdown(f"**{sender_label}** at {timestamp[:19]}:\n> {message}")

    # Mark messages as read
    client.mark_as_read(username, receiver)

    # Message input
    st.markdown("### ✉️ Send Message")
    user_msg = st.text_input("Type your message", key="msg_input")
    if st.button("Send"):
        if user_msg.strip():
            client.send_message(username, receiver, user_msg)
            st.rerun()
        else:
            st.warning("Message cannot be empty.")

