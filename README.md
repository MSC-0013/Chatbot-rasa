# Chatbot Interface with Streamlit

This project provides a simple and clean chatbot interface using Streamlit, integrated with a Rasa backend. Users can interact with the chatbot, and responses are displayed in a stylish, user-friendly manner.

## Features

- **Interactive Chatbot Interface**: Communicate with a Rasa-powered chatbot.
- **Clean Design**: Modern and simple design with a sidebar and stylish responses.
- **Loading Indicator**: Visual feedback while waiting for the bot’s response.

## Prerequisites

Before running the application, make sure you have:

- Python 3.7 or later installed.
- Rasa server running locally at `http://localhost:5005`.

## Installation

1. **Clone the repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/chatbot-streamlit.git
    cd chatbot-streamlit
    ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install required packages**:

    ```bash
    pip install streamlit requests
    ```

4. **Save your Rasa server URL**:

    Ensure your Rasa server is running on `http://localhost:5005`. Adjust the `RASA_URL` in the code if necessary.

## Running the Application

1. **Save the Streamlit app code**:

    Save the following code to `chatbot_app.py`:

    ```python
    import streamlit as st
    import requests

    # URL of your Rasa server
    RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

    def send_message(message, sender='user'):
        """Send a message to the Rasa server and return the response."""
        response = requests.post(RASA_URL, json={'sender': sender, 'message': message})
        return response.json()

    # Set up the Streamlit page
    st.set_page_config(page_title="Chatbot Interface", page_icon=":robot_face:", layout="wide")

    # Sidebar with title
    with st.sidebar:
        st.title("Chatbot Assistant")
        st.write("Interact with the chatbot and get responses.")

    st.title("Chat with Rasa Bot")
    st.subheader("Ask your question below:")

    # Create a form for input
    with st.form(key='chat_form'):
        user_input = st.text_input("You:", "")
        submit_button = st.form_submit_button(label='Send')

    # Display bot response when button is clicked
    if submit_button and user_input:
        with st.spinner("Bot is thinking..."):
            response = send_message(user_input)
            st.write("### Bot Response:")
            for message in response:
                bot_message = message.get('text', '')
                st.markdown(f"**🤖 {bot_message}**")

    st.write("Type a message and press 'Send' to chat with the bot.")
    ```

2. **Run the Streamlit app**:

    ```bash
    streamlit run chatbot_app.py
    ```

3. **Open your browser** and navigate to `http://localhost:8501` to interact with the chatbot.

## Troubleshooting

- **Rasa Server Not Running**: Ensure that your Rasa server is up and running on the specified URL.
- **Network Issues**: Check for any network issues that might prevent communication between Streamlit and the Rasa server.
- **Dependencies**: Make sure all required Python packages are installed correctly.

## Contributing

Feel free to contribute by submitting issues, feature requests, or pull requests. For detailed information on contributing, refer to the
