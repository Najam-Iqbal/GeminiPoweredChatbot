import streamlit as st
import google.generativeai as genai
import os
#Enter your secret key here
genai.configure(api_key=st.secrets.sec_key.Gemini_aug)

model = genai.GenerativeModel('gemini-1.5-flash')
# Setting up the page configuration
st.set_page_config(
    page_title="Chat with GPT-2",
    page_icon="💬",
    layout="wide",
)

# Header with a custom title and subheader
st.title("💬 Chat with Smartbot")
st.subheader("A conversational AI powered by Gemini")

st.markdown("---")

# Introductory message
st.write(
    "Welcome! Ask me anything or start a conversation. I'm here to chat with you. "
    "Type your message below and press 'Send'."
)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input field for the user's message
user_input = st.text_input("You:", placeholder="Type your message here...")

# Adding a button with custom styling
if st.button("Send 💬"):
    if user_input.strip():  # Check if the user input is not just empty spaces
        try:
            # Append the user's message to the chat history
            st.session_state.chat_history.append(f"**You:** {user_input}")
            
            # respons given by Gemini model
            response = model.generate_content(
            user_input,
            generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=2000,
            temperature=2.0,
                                   ),
                                               )

            
            # Append the bot's response to the chat history
            st.session_state.chat_history.append(f"**Bot:** {response.text}")
            
            # Clear the input field after sending the message
            st.session_state.user_input = "" 
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a message.")

# Display chat history
for message in st.session_state.chat_history:
    st.write(message)

# Adding some spacing and a footer with information
st.markdown("---")
st.write("💡 Powered by Gemini| Built with [Streamlit](https://streamlit.io/)")