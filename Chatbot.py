import streamlit as st
import requests

RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

def send_message(message, sender='user'):
    response = requests.post(RASA_URL, json={'sender': sender, 'message': message})
    return response.json()

st.set_page_config(page_title="Chatbot Interface", page_icon=":robot_face:", layout="wide")

with st.sidebar:
    st.title("Chatbot Assistant")

st.title("Chat with Rasa Bot")
st.subheader("Ask your question below:")

with st.form(key='chat_form'):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    with st.spinner("Bot is thinking..."):
        response = send_message(user_input)
        st.write("### Bot Response:")
        for message in response:
            bot_message = message.get('text', '')
            st.markdown(f"**🤖 {bot_message}**")

st.write("Type a message and press 'Send' to chat with the bot.")
