import os
from typing import Dict

from dotenv import load_dotenv
import openai

from .retry import retry


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@retry(max_retries=1, delay=3)
def call_openai(prompt: str):
    return openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a social media copywriter for a financial news brand."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=100,
    )

def rewrite_as_social_post(article: Dict[str, str]) -> str:
    """
    Transforms a news article's headline and summary into a concise, 
    attention-grabbing social media post using the OpenAI GPT-4o model.
    
    Args:
        article (Dict[str, str]): A dictionary with at least two keys:
            - 'title': The news article headline.
            - 'summary': A short sub-head or description of the article.

    Returns:
        str: A rewritten social media post string, ready to publish.
    """

    title = article["title"]
    summary = article["summary"]

    prompt = (
f"""Turn the following headline and summary into a short, punchy social media post.

It should include a bold hook and a clear call-to-action. Keep it under 200 characters.

DO NOT INCLUDE ANY LINKS OR PLACEHOLDERS LIKE '[Link]' IN THE OUTPUT.
---
## Headline: 
{title}
---
## Summary: 
{summary}
---
Social Media Post:"""
    )

    response = call_openai(prompt=prompt)

    reply = response.choices[0].message.content
    return reply
