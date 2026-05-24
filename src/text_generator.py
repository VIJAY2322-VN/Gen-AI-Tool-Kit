"""
Text Generation Module
Generates AI-style text content.
"""

import random

sample_texts = [
    "Artificial Intelligence is transforming industries.",
    "Generative AI helps automate creative tasks.",
    "Machine learning improves decision making."
]

def generate_text():
    return random.choice(sample_texts)

if __name__ == "__main__":
    print(generate_text())