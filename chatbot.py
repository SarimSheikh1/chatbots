import streamlit as st
import random

# Sample responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad you are talking to me"]

# Basic knowledge base for responses
KNOWLEDGE_BASE = {
    "what is python": "Python is a high-level, interpreted programming language known for its easy syntax and versatility.",
    "what is streamlit": "Streamlit is an open-source app framework for Machine Learning and Data Science projects.",
    "what can python do": "Python can be used for web development, data analysis, artificial intelligence, scientific computing, and more.",
    "tell me about python": "Python is designed to be easy to read and write, making it a great choice for beginners and professionals alike."
}

# Function to return a greeting response
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Simple bot response generator
def get_response(user_response):
    user_response = user_response.lower()

    # Check for greeting
    if greeting(user_response) is not None:
        return greeting(user_response)
    
    # Check knowledge base for a response
    response = KNOWLEDGE_BASE.get(user_response, "I don't understand. Can you please rephrase?")
    return response

# Streamlit App
def main():
    # Streamlit layout
    st.title("Simple Chatbot")
    st.write("Type your message and the chatbot will respond.")

    # Session State to store chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Input area
    user_input = st.text_input("You:", "")

    if user_input:
        response = get_response(user_input)
        # Store the conversation
        st.session_state.history.append((user_input, response))

    # Display chat history
    for user_message, bot_response in st.session_state.history:
        st.write(f"You: {user_message}")
        st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
#streamlit run c:/Users/sarim/GI/chatbot.py
