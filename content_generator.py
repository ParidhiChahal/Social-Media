"""
Social Media Content Generator
Author: Paridhi chahal
Roll No: 2301730186

Description:
An AI-powered application that automatically generates engaging posts, 
captions, and hashtags for social media platforms using Generative AI models.
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class ContentGenerator:
    def __init__(self, model_name="gpt2"):
        print("Loading model...")
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.model.eval()

    def generate_text(self, prompt, max_new_tokens=100, temperature=0.7, top_k=50):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")

        outputs = self.model.generate(
            inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )

        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result

    def generate_post(self, topic):
        prompt = f"Write an engaging social media post about {topic}:\n"
        return self.generate_text(prompt)

    def generate_caption(self, topic):
        prompt = f"Create a catchy caption for {topic}:\n"
        return self.generate_text(prompt, max_new_tokens=50)

    def generate_hashtags(self, topic):
        prompt = f"Generate trending hashtags for {topic}:\n"
        return self.generate_text(prompt, max_new_tokens=30)


# CLI usage
if __name__ == "__main__":
    generator = ContentGenerator()

    topic = input("Enter a topic: ")

    print("\n--- Generated Post ---")
    print(generator.generate_post(topic))

    print("\n--- Caption ---")
    print(generator.generate_caption(topic))

    print("\n--- Hashtags ---")
    print(generator.generate_hashtags(topic))
