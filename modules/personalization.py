import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_1")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def personalization_css():
    st.markdown("""
    <style>
    .personalization-card {
        padding: 25px;
        border-radius: 18px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    .personalization-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .personalization-text {
        font-size: 16px;
        line-height: 1.6;
        color: #475569;
    }
    </style>
    """, unsafe_allow_html=True)


def personalize_learning(
    student_name,
    learning_level,
    subject,
    topic,
    goal,
    study_time,
    learning_style
):

    prompt = f"""
You are BrainByte, a personal AI tutor.

Student: {student_name}
Learning Level: {learning_level}
Subject: {subject}
Topic: {topic}
Goal: {goal}
Daily Study Time: {study_time}
Learning Style: {learning_style}

Create a personalized study plan.

Give:
1. Suitable learning approach
2. Main concepts to focus on
3. Recommended difficulty
4. Short study plan
5. Practice recommendation

Keep it simple and suitable for the student's level.
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating personalized plan: {e}"