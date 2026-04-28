from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class AdRequest(BaseModel):
    business_type: str
    audience: str
    product: str
    platform: str

@app.get("/")
def home():
    return {"message": "AI Ad Generator API is running"}

@app.post("/generate_ad")
def generate_ad(data: AdRequest):
    prompt = f"""
You are a high-converting ad copywriter.

Business Type: {data.business_type}
Target Audience: {data.audience}
Product/Service: {data.product}
Platform: {data.platform}

Generate:
1. 3 scroll-stopping hooks (max 8 words)
2. 1 emotional ad script (15–30 seconds)
3. 1 problem-agitate-solution copy
4. 1 CTA with urgency

Style:
- Simple language
- Emotional + persuasive
- Focus on benefits
- Add curiosity gap

Output format:
Hooks:
1.
2.
3.

Script:

Ad Copy:

CTA:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"ad": response.choices[0].message.content}
