from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(api_key=os.getenv("GROQ_API_KEY"),
              base_url="https://api.groq.com/openai/v1"
              )

def generate_response(prompt: str,context:str)->str:
    response=client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":f"Context: {context}\n\nQuestion: {prompt}"}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()