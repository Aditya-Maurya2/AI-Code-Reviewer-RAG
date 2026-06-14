import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(
    api_key=os.getenv("AIzaSyCslgh4eZAYDFmEFZYDZHDvJvvEaEQe44E")
)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def review_code(context, query):

    prompt = f"""
You are an expert code reviewer.

Code:
{context}

User Question:
{query}

Provide:
1. Bugs
2. Security Issues
3. Performance Improvements
4. Best Practices
5. Fixed Code (if needed)
"""

    response = model.generate_content(prompt)

    return response.text