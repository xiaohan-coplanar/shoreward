import streamlit as st
import requests

st.set_page_config(page_title="Travel Assistant", page_icon="✈️", layout="wide")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# API configuration
API_URL = "http://localhost:8000/chat"  # Adjust according to your backend

# Page title
st.title("✈️ Travel Planning Assistant")
st.markdown("_Use this chatbot to help plan your trip._")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Enter your travel question...")

if user_input:
    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add the new message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Prepare request content
    chat_history = [
        {"role": msg["role"], "content": msg["content"]} 
        for msg in st.session_state.messages[:-1]  # Exclude the latest user message
    ]
    
    request_data = {
        "message": user_input,
        "history": chat_history
    }
    
    # Display assistant "thinking" placeholder
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Call the API
            response = requests.post(API_URL, json=request_data, stream=True)
            response.raise_for_status()  # Raise exception on request failure
            
            # Get the reply
            reply = ""
            for line in response.iter_content():
                if line:
                    decoded_line = line.decode('utf-8')
                    reply += decoded_line
                    message_placeholder.markdown(reply)
            
            # Add the reply to chat history
            st.session_state.messages.append({"role": "assistant", "content": reply})
            
        except Exception as e:
            message_placeholder.markdown(f"An error occurred: {str(e)}")
