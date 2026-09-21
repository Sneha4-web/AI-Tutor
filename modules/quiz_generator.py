import streamlit as st
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = st.secrets["API_KEY_2"]

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def quiz_css():
    st.markdown("""
    <style>
    .quiz-card {
        padding: 25px;
        border-radius: 18px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .quiz-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .quiz-info {
        padding: 12px;
        border-radius: 10px;
        background: #f1f5f9;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)


def generate_quiz(subject, topic, difficulty):

    prompt = f"""
Create exactly 5 multiple-choice questions for a student.

Subject: {subject}
Topic: {topic}
Difficulty: {difficulty}

Return ONLY valid JSON:

{{
    "questions": [
        {{
            "question": "Question here",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": 0,
            "concept": "Concept name"
        }}
    ]
}}

Rules:
- Exactly 5 questions
- Exactly 4 options per question
- answer must be 0, 1, 2, or 3
- Include the concept being tested
- Do not add anything outside the JSON
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        text = response.choices[0].message.content
        return json.loads(text)

    except Exception as e:
        return {"error": str(e)}
