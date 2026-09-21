import streamlit as st

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Student Profile - BrainByte",
    page_icon="👤",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4b3f9b;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666666;
    margin-bottom: 35px;
}

.section-title {
    font-size: 24px;
    font-weight: bold;
    color: #4b3f9b;
    margin-top: 20px;
    margin-bottom: 10px;
}

.profile-card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.success-card {
    background-color: #E64A45;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #28a745;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="title">🧠 BrainByte</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Personal AI Tutor - Create Your Learning Profile</div>',
    unsafe_allow_html=True
)

# =========================================================
# SESSION STATE
# =========================================================

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "age" not in st.session_state:
    st.session_state.age = 18

if "student_class" not in st.session_state:
    st.session_state.student_class = ""

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "goal" not in st.session_state:
    st.session_state.goal = ""

if "study_time" not in st.session_state:
    st.session_state.study_time = ""

if "learning_style" not in st.session_state:
    st.session_state.learning_style = ""

if "profile_created" not in st.session_state:
    st.session_state.profile_created = False

# =========================================================
# PROFILE INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Basic Information</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

name = st.text_input(
    "Your Name",
    value=st.session_state.student_name,
    placeholder="Enter your name"
)

age = st.number_input(
    "Your Age",
    min_value=5,
    max_value=100,
    value=st.session_state.age,
    step=1
)

learning_level = st.text_input(
    "Class / Learning Level",
    value=st.session_state.student_class,
    placeholder="Example: Class 10, College, University, Beginner, Professional"
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SUBJECT
# =========================================================

st.markdown(
    '<div class="section-title">📚 What Do You Want to Learn?</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

subject_input = st.text_input(
    "Enter Your Subject",
    placeholder="Example: Mathematics, Physics, History, Python, Biology..."
)

st.markdown(
    "You can enter **any subject** you want to learn.",
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# LEARNING GOAL
# =========================================================

st.markdown(
    '<div class="section-title">🎯 Your Learning Goal</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

goal = st.selectbox(
    "What is your main goal?",
    [
        "Understand Concepts",
        "Prepare for an Exam",
        "Improve My Skills",
        "Learn Something New",
        "Complete Homework",
        "Prepare for Competitive Exam",
        "Professional Learning"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# STUDY TIME
# =========================================================

st.markdown(
    '<div class="section-title">⏰ Study Time</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

study_time = st.selectbox(
    "How much time can you study every day?",
    [
        "15 minutes",
        "30 minutes",
        "1 hour",
        "1-2 hours",
        "2-3 hours",
        "More than 3 hours"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# LEARNING STYLE
# =========================================================

st.markdown(
    '<div class="section-title">🧩 Learning Style</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

learning_style = st.selectbox(
    "How do you like to learn?",
    [
        "Simple Explanation",
        "Real-Life Examples",
        "Step-by-Step Explanation",
        "Exam Focused",
        "Detailed Explanation",
        "Practice Based"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# SAVE PROFILE
# =========================================================

st.markdown("---")

if st.button("💾 Save Profile", use_container_width=True):

    if name.strip() == "":
        st.error("Please enter your name.")

    elif learning_level.strip() == "":
        st.error("Please enter your class or learning level.")

    elif subject_input.strip() == "":
        st.error("Please enter a subject.")

    else:

        # Save information in Streamlit session
        st.session_state.student_name = name
        st.session_state.age = age
        st.session_state.student_class = learning_level
        st.session_state.subjects = [subject_input]
        st.session_state.goal = goal
        st.session_state.study_time = study_time
        st.session_state.learning_style = learning_style

        # Save subject for Learning page
        st.session_state.selected_subject = subject_input

        st.session_state.profile_created = True

        st.success("✅ Your profile has been saved successfully!")

# =========================================================
# PROFILE SUMMARY
# =========================================================

if st.session_state.profile_created:

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📋 Your Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="success-card">

        <h3>Welcome, {st.session_state.student_name}! 👋</h3>

        <p><b>Age:</b> {st.session_state.age}</p>

        <p><b>Class / Learning Level:</b>
        {st.session_state.student_class}</p>

        <p><b>Subject:</b>
        {st.session_state.selected_subject}</p>

        <p><b>Learning Goal:</b>
        {st.session_state.goal}</p>

        <p><b>Daily Study Time:</b>
        {st.session_state.study_time}</p>

        <p><b>Learning Style:</b>
        {st.session_state.learning_style}</p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # =====================================================
    # START LEARNING BUTTON
    # =====================================================

    if st.button(
        "🚀 Start Learning",
        use_container_width=True
    ):

        st.switch_page("pages/learning.py")