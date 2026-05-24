"""
Image Generator Module
Simulates AI image generation prompts.
"""

def generate_image(prompt):
    return f"Image generated successfully for prompt: '{prompt}'"

if __name__ == "__main__":
    prompt = input("Enter image prompt: ")
    print(generate_image(prompt))