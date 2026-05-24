"""
AI Chatbot Module
This module provides a simple AI chatbot response system.
"""

def chatbot_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm functioning perfectly!",
        "bye": "Goodbye! Have a great day."
    }

    return responses.get(user_input.lower(), "Sorry, I don't understand.")

if __name__ == "__main__":
    user = input("You: ")
    print("Bot:", chatbot_response(user))