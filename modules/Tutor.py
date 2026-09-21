import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = st.secrets["API_KEY_4"]

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)



def tutor_css():
    st.markdown("""
    <style>
    .tutor-card {
        padding: 25px;
        border-radius: 18px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    .tutor-title {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .tutor-subtitle {
        font-size: 17px;
        color: #64748b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


def generate_lesson(
    student_name,
    learning_level,
    subject,
    topic,
    goal,
    study_time,
    learning_style,
    difficulty
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
Difficulty: {difficulty}

Create a personalized lesson.

Include:
1. What You Will Learn
2. Introduction
3. Main Concept
4. Simple Example
5. Important Points
6. Quick Practice with 3 questions

Make the explanation suitable for the student's level.
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are BrainByte, a helpful personal AI tutor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating lesson: {e}"