from transformers import pipeline
import random

# Load small HuggingFace text-generation model
generator = pipeline('text-generation', model='gpt2', device=-1)  # device=-1 -> CPU

# You can keep a fallback list in case generation fails
fallback_ideas = [
    "Python 5 lines to create a QR code generator",
    "AI model to detect your mood using camera",
    "Simple voice recognition in Python",
    "How to control mouse with your hand using OpenCV"
]

def get_random_idea():
    try:
        prompt = "Tech idea for a short YouTube video: "
        output = generator(prompt, max_length=30, num_return_sequences=1)
        idea = output[0]['generated_text'].replace(prompt, "").strip()
        return idea if len(idea) > 5 else random.choice(fallback_ideas)
    except:
        return random.choice(fallback_ideas)
