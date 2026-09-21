import streamlit as st

from modules.Tutor import generate_lesson

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="BrainByte AI Tutor",
    page_icon="🧠",
    layout="wide"
)


# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

body {
    background-color: #f5f7fb;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #4b3f9b;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666666;
    margin-bottom: 30px;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.lesson-card {
    background-color: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    margin-top: 25px;
}

.section-title {
    color: #4b3f9b;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 10px;
}

.student-badge {
    background-color: #eeeafd;
    padding: 10px 15px;
    border-radius: 10px;
    color: #4b3f9b;
    font-weight: 600;
    margin-bottom: 15px;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    padding: 12px;
    font-size: 17px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🧠 BrainByte</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Personal AI Tutor</div>',
    unsafe_allow_html=True
)


# ==========================================
# GET STUDENT PROFILE
# ==========================================

student_name = st.session_state.get(
    "student_name",
    "Student"
)

learning_level = st.session_state.get(
    "student_class",
    ""
)

subject = st.session_state.get(
    "selected_subject",
    ""
)

topic = st.session_state.get(
    "selected_topic",
    ""
)

goal = st.session_state.get(
    "goal",
    "Understand Concepts"
)

study_time = st.session_state.get(
    "study_time",
    "30 minutes"
)

learning_style = st.session_state.get(
    "learning_style",
    "Simple Explanation"
)

difficulty = st.session_state.get(
    "selected_difficulty",
    "Beginner"
)


# ==========================================
# CHECK INFORMATION
# ==========================================

if subject == "" or topic == "":

    st.warning(
        "Please select a subject and topic on the Learning page first."
    )

    st.stop()


# ==========================================
# STUDENT INFORMATION CARD
# ==========================================

st.markdown(
    '<div class="section-title">👤 Your Personalized Learning Plan</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-card">',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="student-badge">
        👋 Welcome, {student_name}!
    </div>

    <p><b>📚 Subject:</b> {subject}</p>

    <p><b>📖 Topic:</b> {topic}</p>

    <p><b>🎓 Learning Level:</b> {learning_level}</p>

    <p><b>🎯 Goal:</b> {goal}</p>

    <p><b>⏰ Study Time:</b> {study_time}</p>

    <p><b>🧩 Learning Style:</b> {learning_style}</p>

    <p><b>📊 Difficulty:</b> {difficulty}</p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# GENERATE LESSON
# ==========================================

if st.button("✨ Generate My Personalized Lesson"):

    with st.spinner(
        "🧠 BrainByte is preparing your personalized lesson..."
    ):

        try:

            lesson = generate_lesson(
                student_name,
                learning_level,
                subject,
                topic,
                goal,
                study_time,
                learning_style,
                difficulty
            )

            st.session_state.ai_lesson = lesson

        except Exception as e:

            st.error("Unable to generate the lesson.")

            st.write(e)


# ==========================================
# DISPLAY LESSON
# ==========================================

if "ai_lesson" in st.session_state:

    st.markdown(
        '<div class="section-title">📚 Your Personalized Lesson</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="lesson-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state.ai_lesson
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ==========================================
# PRACTICE / QUIZ BUTTON
# ==========================================

if "ai_lesson" in st.session_state:

    st.markdown("---")

    st.info(
        "💡 Finished reading? Test your understanding with a quiz."
    )

    if st.button("🎯 Take a Quiz"):

        st.switch_page("pages/Quiz.py")