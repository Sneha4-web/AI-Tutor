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

/* ==================================================
   BRAINBYTE HOME PAGE
   Light + Dark Streamlit Theme
   ================================================== */


/* ---------- Main App Background ---------- */

.stApp {
    background:
        radial-gradient(
            circle at top left,
            rgba(99, 102, 241, 0.16),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(139, 92, 246, 0.12),
            transparent 35%
        ),
        var(--background-color);
}


/* ---------- Main Content ---------- */

.block-container {
    max-width: 1000px;
    padding-top: 4rem;
    padding-bottom: 3rem;
}


/* ---------- Main Title ---------- */

h1 {
    font-size: 60px !important;
    font-weight: 800 !important;
    margin-bottom: 5px !important;
    letter-spacing: -2px;
    text-align: center;

    background: linear-gradient(
        90deg,
        #6366f1,
        #8b5cf6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}


/* ---------- Subtitle ---------- */

h2 {
    font-size: 28px !important;
    font-weight: 600 !important;
    margin-bottom: 25px !important;
    text-align: center;
    color: var(--text-color) !important;
}


/* ---------- Normal Text ---------- */

.stMarkdown p {
    font-size: 18px;
    line-height: 1.7;
    color: var(--text-color);
}


/* ---------- Feature Cards ---------- */

.feature-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 18px;

    padding: 20px 24px;
    margin: 14px 0;

    color: var(--text-color);

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.08);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


/* ---------- Feature Card Hover ---------- */

.feature-card:hover {
    transform: translateY(-3px);

    box-shadow:
        0 10px 28px rgba(0, 0, 0, 0.14);
}


/* ---------- Horizontal Divider ---------- */

hr {
    border: none !important;

    border-top:
        1px solid rgba(128, 128, 128, 0.25) !important;

    margin: 35px 0 !important;
}


/* ---------- Primary Button ---------- */

.stButton > button {
    border-radius: 14px !important;

    min-height: 52px !important;

    font-size: 17px !important;
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
        0 8px 20px rgba(99, 102, 241, 0.25);

    transition:
        all 0.2s ease-in-out;
}


/* ---------- Button Hover ---------- */

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 28px rgba(99, 102, 241, 0.35);
}


/* ---------- Button Press ---------- */

.stButton > button:active {
    transform: translateY(0px);
}


/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {
    background: var(--secondary-background-color);

    border-right:
        1px solid rgba(128, 128, 128, 0.18);
}


/* ---------- Sidebar Title ---------- */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2 {
    text-align: left;

    color: var(--text-color) !important;
}


/* ---------- Sidebar Text ---------- */

section[data-testid="stSidebar"] p {
    color: var(--text-color) !important;
}


/* ---------- Footer ---------- */

.footer {
    margin-top: 70px;

    padding-top: 20px;

    border-top:
        1px solid rgba(128, 128, 128, 0.22);

    color:
        rgba(128, 128, 128, 0.9);

    font-size: 14px;

    text-align: center;
}


/* ==================================================
   DARK MODE
   ================================================== */

@media (prefers-color-scheme: dark) {

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(99, 102, 241, 0.18),
                transparent 35%
            ),
            radial-gradient(
                circle at bottom right,
                rgba(139, 92, 246, 0.14),
                transparent 35%
            ),
            #0e1117;
    }


    .stMarkdown p {
        color: #d1d5db;
    }


    section[data-testid="stSidebar"] {
        background: #151922;

        border-right-color:
            #292e39;
    }


    .feature-card {
        background: #161b22;

        border-color:
            #30363d;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.35);

        color: #f0f6fc;
    }


    .footer {
        color: #8b949e;

        border-top-color:
            #30363d;
    }
}


/* ==================================================
   MOBILE
   ================================================== */

@media (max-width: 768px) {

    .block-container {
        padding-top: 2.5rem;

        padding-left: 1rem;

        padding-right: 1rem;
    }


    h1 {
        font-size: 42px !important;
    }


    h2 {
        font-size: 23px !important;
    }


    .stMarkdown p {
        font-size: 16px;
    }


    .feature-card {
        padding: 17px;
    }
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
# FEATURES
# --------------------------------------------------

st.markdown("---")

st.markdown("""
<div class="feature-card">
    📚 <b>Learn</b><br>
    Choose your subject and specific topic.
</div>

<div class="feature-card">
    📝 <b>Practice</b><br>
    Take AI-generated quizzes and strengthen your knowledge.
</div>

<div class="feature-card">
    📊 <b>Track</b><br>
    Monitor your learning progress and improve over time.
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# START PROFILE
# --------------------------------------------------

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
    """
    <div class="footer">
        🧠 Brainbyte — Learn smarter. Learn your way.
    </div>
    """,
    unsafe_allow_html=True
)
