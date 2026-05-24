from src.chatbot import chatbot_response
from src.text_generator import generate_text
from src.sentiment import analyze_sentiment
from src.summarizer import summarize_text
from src.image_generator import generate_image

print("===== Generative AI Toolkit =====")

print("\nGenerated Text:")
print(generate_text())

print("\nSentiment Analysis:")
print(analyze_sentiment("This project is excellent"))

print("\nChatbot:")
print(chatbot_response("hello"))

print("\nSummarization:")
text = "AI is growing rapidly. It helps automate tasks. It improves productivity."
print(summarize_text(text))

print("\nImage Generator:")
print(generate_image("Future AI city"))