import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()



st.page_link("pages/dashboard.py", label="Progress Hub",
             icon="📈")


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="BrainByte AI Quiz",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: #f5f7fb;
    }

    /* Header */
    .quiz-header {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #667eea,
            #764ba2
        );
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.10);
    }

    .quiz-header h1 {
        font-size: 40px;
        margin-bottom: 5px;
    }

    .quiz-header p {
        font-size: 17px;
        margin: 0;
    }

    /* Question cards */
    .quiz-card {
        padding: 22px;
        margin: 15px 0;
        border-radius: 18px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 15px rgba(0,0,0,0.06);
    }

    /* Result card */
    .result-card {
        padding: 25px;
        margin-top: 20px;
        border-radius: 18px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 15px rgba(0,0,0,0.06);
    }

    .score-number {
        font-size: 45px;
        font-weight: bold;
    }

    /* Weak concepts */
    .weak-card {
        padding: 20px;
        margin-top: 20px;
        border-radius: 15px;
        background: #fff5f5;
        border-left: 5px solid #ff4b4b;
    }

    /* Strong concepts */
    .strong-card {
        padding: 20px;
        margin-top: 20px;
        border-radius: 15px;
        background: #f0fff4;
        border-left: 5px solid #21c55d;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# GROQ API
# ============================================================

API_KEY = st.secrets["API_KEY_5"]

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


# ============================================================
# SESSION STATE
# ============================================================

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = None

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0


# ============================================================
# GET STUDENT INFORMATION
# ============================================================

student_name = st.session_state.get(
    "student_name",
    "Student"
)

subject = st.session_state.get(
    "selected_subject",
    ""
)

topic = st.session_state.get(
    "selected_topic",
    ""
)

difficulty = st.session_state.get(
    "selected_difficulty",
    "Beginner"
)

learning_style = st.session_state.get(
    "selected_learning_style",
    "Simple Explanation"
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="quiz-header">

        <h1>🧠 BrainByte AI Quiz</h1>

        <p>
            Test your understanding with an AI-generated
            personalized quiz.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CHECK SUBJECT / TOPIC
# ============================================================

if not subject or not topic:

    st.warning(
        "Please select a subject and topic from the Learning page first."
    )

    st.stop()


st.write(
    f"**Student:** {student_name}"
)

st.write(
    f"**Subject:** {subject}"
)

st.write(
    f"**Topic:** {topic}"
)

st.write(
    f"**Difficulty:** {difficulty}"
)


# ============================================================
# AI QUIZ GENERATOR
# ============================================================

def generate_ai_quiz():

    prompt = f"""
You are BrainByte, a personal AI tutor.

Create a quiz for this student.

Student:
{student_name}

Subject:
{subject}

Topic:
{topic}

Difficulty:
{difficulty}

Learning style:
{learning_style}

Create exactly 5 multiple-choice questions.

Each question must have exactly 4 answer options.

Return ONLY valid JSON using this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": [
                "Option 1",
                "Option 2",
                "Option 3",
                "Option 4"
            ],
            "answer": 0,
            "concept": "Concept being tested"
        }}
    ]
}}

Rules:

1. Create exactly 5 questions.
2. Each question must have exactly 4 options.
3. "answer" must be 0, 1, 2, or 3.
4. "answer" represents the position of the correct option.
5. Questions must match the subject and topic.
6. Questions must match the difficulty.
7. Include different concepts where possible.
8. Do not include explanations.
9. Do not include answers outside the JSON.
"""


    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are BrainByte, "
                        "a helpful personal AI tutor."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.4,

            response_format={
                "type": "json_object"
            }
        )


        content = response.choices[0].message.content

        data = json.loads(content)

        questions = data.get(
            "questions",
            []
        )


        # Validate question count

        if len(questions) != 5:

            st.error(
                "AI did not generate exactly 5 questions."
            )

            return None


        # Validate every question

        for question in questions:

            if "question" not in question:
                return None

            if "options" not in question:
                return None

            if "answer" not in question:
                return None

            if len(question["options"]) != 4:
                return None

            if question["answer"] not in [0, 1, 2, 3]:
                return None


        return questions


    except Exception as e:

        st.error(
            f"Groq API error: {e}"
        )

        return None


# ============================================================
# GENERATE QUIZ
# ============================================================

if st.session_state.quiz_questions is None:

    if st.button(
        "🧠 Generate AI Quiz",
        use_container_width=True,
        type="primary"
    ):

        with st.spinner(
            "BrainByte is creating your personalized quiz..."
        ):

            questions = generate_ai_quiz()


        if questions:

            st.session_state.quiz_questions = questions

            st.session_state.quiz_submitted = False

            st.session_state.quiz_score = 0

            st.rerun()


# ============================================================
# LOAD QUESTIONS
# ============================================================

questions = st.session_state.quiz_questions


if questions is None:

    st.stop()


# ============================================================
# QUIZ FORM
# ============================================================

with st.form("brainbyte_quiz_form"):

    user_answers = []


    for i, question in enumerate(questions):

        st.markdown(
            '<div class="quiz-card">',
            unsafe_allow_html=True
        )


        st.markdown(
            f"### Question {i + 1}"
        )


        st.write(
            question["question"]
        )


        answer = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"question_{i}",
            index=None
        )


        user_answers.append(answer)


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


    # IMPORTANT:
    # Keep this INSIDE the form.
    # Keep it OUTSIDE the for loop.

    submitted = st.form_submit_button(
        "📝 Submit Quiz",
        use_container_width=True,
        type="primary"
    )


# ============================================================
# CHECK ANSWERS
# ============================================================

if submitted:

    score = 0

    weak_concepts = []

    strong_concepts = []

    unanswered = False


    for i, question in enumerate(questions):

        selected_answer = user_answers[i]


        if selected_answer is None:

            unanswered = True

            continue


        correct_index = question["answer"]

        correct_answer = question["options"][correct_index]

        concept = question.get(
            "concept",
            "General"
        )


        if selected_answer == correct_answer:

            score += 1

            strong_concepts.append(
                concept
            )

        else:

            weak_concepts.append(
                concept
            )


    # ========================================================
    # UNANSWERED
    # ========================================================

    if unanswered:

        st.warning(
            "Please answer every question before submitting."
        )


    # ========================================================
    # RESULT
    # ========================================================

    else:

        percentage = (
            score / len(questions)
        ) * 100


        st.session_state.quiz_score = score

        st.session_state.quiz_submitted = True


        st.markdown(
            """
            <div class="result-card">
            """,
            unsafe_allow_html=True
        )


        st.subheader(
            "🎯 Your Quiz Result"
        )


        st.markdown(
            f"""
            <div class="score-number">
                {score}/{len(questions)}
            </div>
            """,
            unsafe_allow_html=True
        )


        st.write(
            f"Percentage: **{percentage:.0f}%**"
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        # ====================================================
        # WEAK CONCEPTS
        # ====================================================

        if weak_concepts:

            st.markdown(
                """
                <div class="weak-card">

                <h3>🔧 Concepts to Improve</h3>

                """,
                unsafe_allow_html=True
            )


            for concept in weak_concepts:

                st.write(
                    f"• {concept}"
                )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        # ====================================================
        # STRONG CONCEPTS
        # ====================================================

        if strong_concepts:

            st.markdown(
                """
                <div class="strong-card">

                <h3>💪 Strong Concepts</h3>

                """,
                unsafe_allow_html=True
            )


            for concept in strong_concepts:

                st.write(
                    f"• {concept}"
                )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        # ====================================================
        # SAVE PROGRESS
        # ====================================================

        file_path = "data/progress.csv"


        student_id = st.session_state.get(
            "student_id",
            student_name
        )


        new_data = pd.DataFrame(
            [
                {
                    "student_id": student_id,
                    "subject": subject,
                    "topic": topic,
                    "quiz_score": percentage,
                    "attempts": 1,
                    "date": datetime.now().strftime(
                        "%Y-%m-%d"
                    )
                }
            ]
        )


        try:

            if os.path.exists(file_path):

                progress = pd.read_csv(
                    file_path
                )


                progress = pd.concat(
                    [
                        progress,
                        new_data
                    ],
                    ignore_index=True
                )


            else:

                progress = new_data


            progress.to_csv(
                file_path,
                index=False
            )


        except Exception as e:

            st.warning(
                f"Could not save progress: {e}"
            )


# ============================================================
# ANOTHER QUIZ
# ============================================================

if st.session_state.quiz_submitted:

    st.divider()


    if st.button(
        "🔄 Generate Another AI Quiz",
        use_container_width=True
    ):

        st.session_state.quiz_questions = None

        st.session_state.quiz_submitted = False

        st.session_state.quiz_score = 0

        st.rerun()
