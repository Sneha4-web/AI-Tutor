import streamlit as st


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="BrainByte - Learning",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Header */
.learning-header {
    text-align: center;
    padding: 25px;
    margin-bottom: 25px;
}

.learning-header h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
}

.learning-header p {
    font-size: 18px;
    color: #666;
}

/* Main card */
.learning-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    margin-bottom: 25px;
}

/* Info box */
.info-box {
    background: #eef3ff;
    padding: 18px;
    border-radius: 14px;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
}

/* Footer */
.footer {
    text-align: center;
    color: #777;
    margin-top: 35px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="learning-header">
    <h1>📚 Start Learning</h1>
    <p>Choose your subject and the exact topic you want to learn.</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TOPIC DATABASE
# --------------------------------------------------

topics = {
    "Python": [
        "Variables and Data Types",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Lists",
        "Tuples",
        "Dictionaries",
        "Sets",
        "File Handling",
        "Object-Oriented Programming",
        "Exception Handling",
        "Modules and Packages"
    ],

    "Physics": [
        "Motion",
        "Newton's Laws of Motion",
        "Work and Energy",
        "Gravitation",
        "Waves",
        "Electricity",
        "Magnetism",
        "Optics"
    ],

    "Mathematics": [
        "Algebra",
        "Linear Equations",
        "Quadratic Equations",
        "Trigonometry",
        "Coordinate Geometry",
        "Probability",
        "Statistics",
        "Calculus"
    ],

    "Biology": [
        "Cell Structure",
        "Cell Division",
        "Photosynthesis",
        "Respiration",
        "Human Digestive System",
        "Human Circulatory System",
        "Genetics",
        "Evolution"
    ],

    "Chemistry": [
        "Atomic Structure",
        "Periodic Table",
        "Chemical Bonding",
        "Chemical Reactions",
        "Acids and Bases",
        "Mole Concept",
        "Thermodynamics",
        "Organic Chemistry"
    ],

    "History": [
        "Ancient Civilizations",
        "Medieval History",
        "World War I",
        "World War II",
        "Indian Independence",
        "French Revolution",
        "Industrial Revolution"
    ],

    "Computer Science": [
        "Algorithms",
        "Data Structures",
        "Computer Networks",
        "Operating Systems",
        "Database Management",
        "Cyber Security",
        "Artificial Intelligence"
    ]
}


# --------------------------------------------------
# MAIN LEARNING CARD
# --------------------------------------------------

st.markdown("""
<div class="learning-card">
    <h2>🎯 Choose What You Want to Learn</h2>
    <p>
        BrainByte lets you choose the specific topic you want to study.
        You are not limited to Introduction or Basic Concepts.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SUBJECT
# --------------------------------------------------

subject = st.selectbox(
    "📘 Select Subject",
    [
        "Python",
        "Physics",
        "Mathematics",
        "Biology",
        "Chemistry",
        "History",
        "Computer Science",
        "Other"
    ]
)


# --------------------------------------------------
# TOPIC
# --------------------------------------------------

if subject == "Other":

    topic = st.text_input(
        "🎯 Enter Your Topic",
        placeholder="Example: Economics, Geography, Psychology..."
    )

else:

    available_topics = topics[subject]

    topic = st.selectbox(
        "🎯 Select Topic",
        available_topics
    )


# --------------------------------------------------
# EXTRA INFORMATION
# --------------------------------------------------

st.markdown("""
<div class="info-box">
    💡 <b>Example:</b><br>
    Subject: Python<br>
    Topic: Functions<br>
    BrainByte will create a lesson specifically about Python Functions.
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DIFFICULTY
# --------------------------------------------------

difficulty = st.selectbox(
    "📊 Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert"
    ]
)


# --------------------------------------------------
# EXPLANATION STYLE
# --------------------------------------------------

learning_style = st.selectbox(
    "🧠 How should BrainByte explain the topic?",
    [
        "Simple Explanation",
        "Real-Life Examples",
        "Exam Focused",
        "Detailed Explanation",
        "Step-by-Step Explanation"
    ]
)


# --------------------------------------------------
# START LEARNING BUTTON
# --------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button(
    "🚀 Start Learning",
    use_container_width=True,
    type="primary"
):

    if not topic or not topic.strip():

        st.warning("⚠️ Please select or enter a topic.")

    else:

        # Save information for AI Tutor
        st.session_state.selected_subject = subject
        st.session_state.selected_topic = topic
        st.session_state.selected_difficulty = difficulty
        st.session_state.selected_learning_style = learning_style

        # Open AI Tutor
        st.switch_page("pages/AI_Tutor.py")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    🧠 BrainByte — Learn what you want, at your level.
</div>
""", unsafe_allow_html=True)