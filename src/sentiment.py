"""
Sentiment Analysis Module
Detects sentiment from text.
"""

def analyze_sentiment(text):
    positive_words = ["good", "happy", "excellent", "great"]
    negative_words = ["bad", "sad", "terrible", "worst"]

    text = text.lower()

    for word in positive_words:
        if word in text:
            return "Positive Sentiment"

    for word in negative_words:
        if word in text:
            return "Negative Sentiment"

    return "Neutral Sentiment"

if __name__ == "__main__":
    user_text = input("Enter text: ")
    print(analyze_sentiment(user_text))