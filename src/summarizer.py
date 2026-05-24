"""
Text Summarization Module
Provides short summaries from long text.
"""

def summarize_text(text):
    sentences = text.split(".")
    return ".".join(sentences[:2]) + "."

if __name__ == "__main__":
    sample = """
    Generative AI is a branch of artificial intelligence.
    It creates content automatically.
    It is widely used in chatbots and automation.
    """

    print(summarize_text(sample))