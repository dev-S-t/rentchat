import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

class GeminiWrapper:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.history = []
        self.system_prompt = (
            "**Assistant Role Description**:\n\n"
            "You are a helpful chatbot that assists users with Rental Agreement Complexity. "
            "Help them with their queries and provide search results for the most updated information related to their region. "
            "Always ask them about their region if it is not specified."
        )
        
    def chat(self, user_input):
        """Process user input and return a response"""
        # If this is the first message, add the system prompt
        if not self.history:
            self.history.append({"role": "system", "parts": [self.system_prompt]})
        
        # Add user input to history
        self.history.append({"role": "user", "parts": [user_input]})
        
        # Generate response
        response = self.model.generate_content(self.history)
        
        # Add assistant response to history
        self.history.append({"role": "assistant", "parts": [response.text]})
        
        return response.text
    
    def reset_chat(self):
        """Reset the chat history"""
        self.history = []
        
def main():
    # Create an instance of the wrapper
    chatbot = GeminiWrapper()
    
    print("Rental Agreement Assistant (type 'exit' to quit, 'reset' to start over)")
    print("-------------------------------------------------------------------")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'reset':
            chatbot.reset_chat()
            print("Chat history has been reset.")
            continue
        
        try:
            response = chatbot.chat(user_input)
            print("\nAssistant:", response, "\n")
        except Exception as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main() 