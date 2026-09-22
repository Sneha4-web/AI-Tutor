import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="BrainByte AI Quiz",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# PROGRESS HUB
# ============================================================

st.page_link(
    "pages/dashboard.py",
    label="Progress Hub",
    icon="📈"
)


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN BACKGROUND
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(99, 102, 241, 0.12),
                transparent 35%
            ),
            radial-gradient(
                circle at bottom right,
                rgba(139, 92, 246, 0.10),
                transparent 35%
            ),
            var(--background-color);
    }


    /* ========================================================
       MAIN CONTENT
       ======================================================== */

    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       NORMAL STREAMLIT CONTAINERS
       ======================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--secondary-background-color) !important;

        border:
            1px solid rgba(
                128,
                128,
                128,
                0.22
            ) !important;

        border-radius: 18px !important;

        padding: 20px 22px !important;

        margin-bottom: 20px !important;

        box-shadow:
            0 6px 20px rgba(
                0,
                0,
                0,
                0.07
            ) !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        min-height: 50px !important;

        border-radius: 13px !important;

        font-size: 16px !important;

        font-weight: 700 !important;

        border: none !important;

        background:
            linear-gradient(
                90deg,
                #6366f1,
                #8b5cf6
            ) !important;

        color: white !important;

        box-shadow:
            0 8px 20px rgba(
                99,
                102,
                241,
                0.25
            );

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 12px 28px rgba(
                99,
                102,
                241,
                0.35
            );
    }


    /* ========================================================
       RADIO BUTTONS
       ======================================================== */

    div[data-testid="stRadio"] label {
        color: var(--text-color) !important;
    }


    /* ========================================================
       PROGRESS HUB LINK
       ======================================================== */

    a {
        color: var(--primary-color) !important;
    }


    /* ========================================================
       DARK MODE
       ======================================================== */

    @media (prefers-color-scheme: dark) {

        .stApp {
            background:
                radial-gradient(
                    circle at top left,
                    rgba(
                        99,
                        102,
                        241,
                        0.18
                    ),
                    transparent 35%
                ),
                radial-gradient(
                    circle at bottom right,
                    rgba(
                        139,
                        92,
                        246,
                        0.14
                    ),
                    transparent 35%
                ),
                #0e1117;
        }


        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #161b22 !important;

            border-color: #30363d !important;

            box-shadow:
                0 8px 25px rgba(
                    0,
                    0,
                    0,
                    0.35
                ) !important;
        }
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-top: 1.5rem;

            padding-left: 1rem;

            padding-right: 1rem;
        }
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

st.title("🧠 BrainByte AI Quiz")

st.write(
    "Test your understanding with an AI-generated "
    "personalized quiz."
)


# ============================================================
# CHECK SUBJECT / TOPIC
# ============================================================

if not subject or not topic:

    st.warning(
        "Please select a subject and topic from the Learning page first."
    )

    st.stop()


# ============================================================
# STUDENT INFORMATION
# ============================================================

with st.container(border=True):

    st.subheader("📋 Quiz Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Student:** {student_name}"
        )

        st.write(
            f"**Subject:** {subject}"
        )

    with col2:

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

        # ----------------------------------------------------
        # Validate question count
        # ----------------------------------------------------

        if len(questions) != 5:

            st.error(
                "AI did not generate exactly 5 questions."
            )

            return None


        # ----------------------------------------------------
        # Validate every question
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # QUESTION CARD
        # ----------------------------------------------------

        with st.container(border=True):

            st.subheader(
                f"Question {i + 1}"
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


        # ----------------------------------------------------
        # RESULT CARD
        # ----------------------------------------------------

        with st.container(border=True):

            st.subheader(
                "🎯 Your Quiz Result"
            )

            st.markdown(
                f"## {score}/{len(questions)}"
            )

            st.write(
                f"Percentage: **{percentage:.0f}%**"
            )


        # ====================================================
        # WEAK CONCEPTS
        # ====================================================

        if weak_concepts:

            with st.container(border=True):

                st.subheader(
                    "🔧 Concepts to Improve"
                )

                for concept in weak_concepts:

                    st.write(
                        f"• {concept}"
                    )


        # ====================================================
        # STRONG CONCEPTS
        # ====================================================

        if strong_concepts:

            with st.container(border=True):

                st.subheader(
                    "💪 Strong Concepts"
                )

                for concept in strong_concepts:

                    st.write(
                        f"• {concept}"
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
