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

.learning-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    margin-bottom: 25px;
}

.info-box {
    background: #eef3ff;
    padding: 18px;
    border-radius: 14px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
}

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
    <p>Choose the exact topic you want to learn.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# CHECK PROFILE SUBJECT
# --------------------------------------------------

if "selected_subject" not in st.session_state:
    st.warning("⚠️ Please create your learning profile first.")

    if st.button("👤 Go to Profile"):
        st.switch_page("pages/Profile.py")

    st.stop()

# Get subject from Profile
profile_subject = st.session_state.selected_subject.strip()

# --------------------------------------------------
# MAIN LEARNING CARD
# --------------------------------------------------

st.markdown("""
<div class="learning-card">
    <h2>🎯 Choose What You Want to Learn</h2>
    <p>
        BrainByte uses the subject from your profile.
        You can choose a specific topic to study.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SUBJECT FROM PROFILE
# --------------------------------------------------

st.markdown("### 📘 Your Subject")

st.info(f"**{profile_subject}**")

subject = profile_subject

# --------------------------------------------------
# TOPIC
# --------------------------------------------------

st.markdown("### 🎯 What do you want to learn?")

topic = st.text_input(
    "Enter a topic",
    placeholder=f"Example: Enter a topic related to {subject}"
)

st.caption(
    f"You can enter any topic related to **{subject}**."
)

# --------------------------------------------------
# EXTRA INFORMATION
# --------------------------------------------------

st.markdown(f"""
<div class="info-box">
    💡 <b>Example:</b><br>
    Subject: {subject}<br>
    Topic: Enter the specific concept you want to learn.<br>
    BrainByte will create a lesson specifically for your selected topic.
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
# START LEARNING
# --------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button(
    "🚀 Start Learning",
    use_container_width=True,
    type="primary"
):

    if not topic.strip():

        st.warning("⚠️ Please enter a topic.")

    else:

        # Save information for AI Tutor
        st.session_state.selected_subject = subject
        st.session_state.selected_topic = topic.strip()
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