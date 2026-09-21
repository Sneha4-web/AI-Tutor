from openai import OpenAI, APITimeoutError
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = st.secrets("API_KEY_3")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)
    timeout=30.0
)


def generate_next_topic(subject, current_topic, difficulty, quiz_score):

    prompt = f"""
You are BrainByte, a personal AI tutor.

Subject: {subject}
Current topic: {current_topic}
Difficulty: {difficulty}
Quiz score: {quiz_score}%

Recommend ONE logical next topic.

Return only:

Next Topic: [topic]

Why: [one short sentence]
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise personal AI tutor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=100
        )

        return response.choices[0].message.content

    except APITimeoutError:
        return "The AI recommendation took too long to respond. Please try again."

    except Exception as e:
        return f"AI recommendation unavailable: {str(e)}"
