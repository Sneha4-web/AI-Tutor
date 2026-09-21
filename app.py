import streamlit as st


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Brainbyte",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef2ff);
}

.block-container {
    max-width: 1000px;
    padding-top: 5rem;
    text-align: center;
}

/* Main title */
h1 {
    font-size: 60px !important;
    font-weight: 800 !important;
    margin-bottom: 5px !important;
}

/* Subtitle */
h2 {
    font-size: 28px !important;
    font-weight: 600 !important;
    margin-bottom: 25px !important;
}

/* Description */
.stMarkdown p {
    font-size: 18px;
    line-height: 1.7;
    color: #555;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #f8f9ff;
}

/* Sidebar title */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2 {
    text-align: left;
}

/* Footer */
.footer {
    margin-top: 70px;
    color: #777;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

st.title("🧠 Brainbyte")

st.subheader("Personal AI Tutor")

st.write(
    "Welcome to Brainbyte, your personal AI Tutor!"
)

st.write(
    "Learn at your own level, practice with AI-generated quizzes, "
    "and track your learning progress."
)


# --------------------------------------------------
# SIMPLE FEATURES
# --------------------------------------------------

st.markdown("---")

st.write("📚 **Learn** — Choose your subject and specific topic.")

st.write("📝 **Practice** — Take AI-generated quizzes.")

st.write("📊 **Track** — Monitor your learning progress.")

#START PROFILE------------------------------------------

st.markdown("---")

st.subheader("🚀 Ready to start learning?")

st.write(
    "Create your profile to personalize your BrainByte learning experience."
)

if st.button(
    "🚀 Create My Profile",
    use_container_width=True,
    type="primary"
):
    st.switch_page("pages/Profile.py")


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🧠 Brainbyte")

st.sidebar.info(
    "Use the sidebar to start learning, take quizzes, "
    "and track your progress."
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">🧠 Brainbyte — Learn smarter. Learn your way.</div>',
    unsafe_allow_html=True
)
