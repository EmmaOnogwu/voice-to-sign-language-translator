from openai import OpenAI
from llm_prompts.gloss_prompt import gloss
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_gloss(sentence):
    
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You convert English text into Sign Language GLOSS."},
            {"role": "user", "content": gloss.replace("{{sentence}}", sentence)}
        ],
        max_tokens=50,
        temperature=0.2
    )

    # NEW correct access style for SDK 1.x+
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    text = "I am going to the market to buy some food"
    gloss = generate_gloss(text)
    print("Gloss Output:", gloss)
