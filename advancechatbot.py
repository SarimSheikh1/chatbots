import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Chatbot:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_response(self, prompt):
        # Encode the input prompt
        input_ids = self.tokenizer.encode(prompt + self.tokenizer.eos_token, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Create an attention mask
        # Generate a response from the model
        output = self.model.generate(
            input_ids,
            max_length=1000,
            num_return_sequences=1,
            attention_mask=attention_mask,
            pad_token_id=self.tokenizer.eos_token_id
        )
        # Decode the output to get the response
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

# Streamlit app
st.title("Chatbot")
st.subheader("Talk to the GPT-2 chatbot!")

# Initialize the chatbot
chatbot = Chatbot()

# Create a text input for user input
user_input = st.text_input("You:", "")

# When the send button is clicked
if st.button("Send"):
    if user_input:
        response = chatbot.generate_response(user_input)
        st.text_area("Chatbot:", response, height=200)
    else:
        st.text_area("Chatbot:", "Please enter a message.", height=200)
