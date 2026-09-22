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
# Works with BOTH light and dark Streamlit themes
# =========================================================

st.markdown("""
<style>

/* ========================================================
   MAIN PAGE
   ======================================================== */

[data-testid="stAppViewContainer"] {
    background: var(--background-color);
}

[data-testid="stHeader"] {
    background: var(--background-color);
}

.main .block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ========================================================
   BRAINBYTE HEADER
   ======================================================== */

.brainbyte-title {
    text-align: center;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--primary-color);
    margin-bottom: 4px;
}

.brainbyte-subtitle {
    text-align: center;
    font-size: 17px;
    color: var(--text-color);
    opacity: 0.65;
    margin-bottom: 38px;
}


/* ========================================================
   SECTION TITLE
   ======================================================== */

.section-title {
    display: flex;
    align-items: center;
    gap: 10px;

    font-size: 24px;
    font-weight: 750;

    color: var(--text-color);

    margin-top: 28px;
    margin-bottom: 14px;
}


/* ========================================================
   PROFILE CARDS
   IMPORTANT:
   These are REAL Streamlit containers created with
   st.container(border=True)
   ======================================================== */

[data-testid="stVerticalBlockBorderWrapper"] {

    background: var(--secondary-background-color);

    border: 1px solid rgba(128, 128, 128, 0.22);

    border-radius: 18px;

    padding: 20px 22px;

    margin-bottom: 20px;

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.08);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {

    box-shadow:
        0 10px 28px rgba(0, 0, 0, 0.12);

    transform: translateY(-1px);
}


/* ========================================================
   INPUT LABELS
   ======================================================== */

label {

    color: var(--text-color) !important;

    font-weight: 600 !important;
}


/* ========================================================
   TEXT INPUT
   ======================================================== */

[data-baseweb="input"] {

    background: var(--background-color) !important;

    border: 1px solid rgba(128, 128, 128, 0.30) !important;

    border-radius: 10px !important;
}

[data-baseweb="input"]:focus-within {

    border-color: var(--primary-color) !important;

    box-shadow:
        0 0 0 1px var(--primary-color) !important;
}

[data-baseweb="input"] input {

    color: var(--text-color) !important;

}


/* ========================================================
   NUMBER INPUT
   ======================================================== */

[data-testid="stNumberInput"] input {

    color: var(--text-color) !important;

    background: var(--background-color) !important;
}


/* ========================================================
   SELECT BOX
   ======================================================== */

[data-baseweb="select"] > div {

    background: var(--background-color) !important;

    border: 1px solid rgba(128, 128, 128, 0.30) !important;

    border-radius: 10px !important;
}

[data-baseweb="select"] span {

    color: var(--text-color) !important;
}


/* ========================================================
   BUTTONS
   ======================================================== */

.stButton > button {

    width: 100%;

    min-height: 46px;

    border-radius: 11px;

    border: 1px solid var(--primary-color);

    background: var(--primary-color);

    color: white;

    font-size: 16px;

    font-weight: 700;

    transition:
        transform 0.15s ease,
        opacity 0.15s ease;
}

.stButton > button:hover {

    opacity: 0.88;

    transform: translateY(-1px);
}


/* ========================================================
   HELP / DESCRIPTION TEXT
   ======================================================== */

[data-testid="stMarkdownContainer"] p {

    color: var(--text-color);
}


/* ========================================================
   PROFILE SUMMARY
   ======================================================== */

.profile-summary {

    background: var(--secondary-background-color);

    border: 1px solid rgba(128, 128, 128, 0.25);

    border-left: 5px solid var(--primary-color);

    border-radius: 16px;

    padding: 24px 26px;

    margin-top: 15px;

    box-shadow:
        0 7px 24px rgba(0, 0, 0, 0.08);
}

.profile-summary h3 {

    color: var(--primary-color);

    margin-top: 0;

    margin-bottom: 20px;
}

.profile-summary p {

    color: var(--text-color);

    margin: 9px 0;

    font-size: 16px;
}


/* ========================================================
   WELCOME MESSAGE
   ======================================================== */

.welcome-box {

    background: var(--secondary-background-color);

    border-radius: 14px;

    padding: 14px 18px;

    border: 1px solid rgba(128, 128, 128, 0.20);

    margin-bottom: 10px;
}

.welcome-box p {

    margin: 0;

    color: var(--text-color);
}


/* ========================================================
   DIVIDERS
   ======================================================== */

hr {

    border-color: rgba(128, 128, 128, 0.25) !important;
}


/* ========================================================
   MOBILE RESPONSIVE DESIGN
   ======================================================== */

@media (max-width: 768px) {

    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .brainbyte-title {
        font-size: 34px;
    }

    .brainbyte-subtitle {
        font-size: 15px;
    }

    .section-title {
        font-size: 21px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 16px;
        border-radius: 14px;
    }
}

</style>
""", unsafe_allow_html=True)


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
# HEADER
# =========================================================

st.markdown(
    '<div class="brainbyte-title">🧠 BrainByte</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="brainbyte-subtitle">'
    'Personal AI Tutor · Create Your Learning Profile'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BASIC INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Basic Information</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

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
        placeholder=(
            "Example: Class 10, College, University, "
            "Beginner, Professional"
        )
    )


# =========================================================
# SUBJECT
# =========================================================

st.markdown(
    '<div class="section-title">📚 What Do You Want to Learn?</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

    subject_input = st.text_input(
        "Enter Your Subject",
        placeholder=(
            "Example: Mathematics, Physics, History, "
            "Python, Biology..."
        )
    )

    st.caption(
        "💡 You can enter any subject you want to learn."
    )


# =========================================================
# LEARNING GOAL
# =========================================================

st.markdown(
    '<div class="section-title">🎯 Your Learning Goal</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

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


# =========================================================
# STUDY TIME
# =========================================================

st.markdown(
    '<div class="section-title">⏰ Study Time</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

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


# =========================================================
# LEARNING STYLE
# =========================================================

st.markdown(
    '<div class="section-title">🧩 Learning Style</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

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


# =========================================================
# SAVE PROFILE
# =========================================================

st.markdown("")


if st.button(
    "💾 Save Profile",
    use_container_width=True
):

    if name.strip() == "":
        st.error("Please enter your name.")

    elif learning_level.strip() == "":
        st.error(
            "Please enter your class or learning level."
        )

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

        st.success(
            "✅ Your profile has been saved successfully!"
        )


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
        <div class="profile-summary">

            <h3>
                Welcome, {st.session_state.student_name}! 👋
            </h3>

            <p>
                <b>Age:</b>
                {st.session_state.age}
            </p>

            <p>
                <b>Class / Learning Level:</b>
                {st.session_state.student_class}
            </p>

            <p>
                <b>Subject:</b>
                {st.session_state.selected_subject}
            </p>

            <p>
                <b>Learning Goal:</b>
                {st.session_state.goal}
            </p>

            <p>
                <b>Daily Study Time:</b>
                {st.session_state.study_time}
            </p>

            <p>
                <b>Learning Style:</b>
                {st.session_state.learning_style}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")


    # =====================================================
    # START LEARNING
    # =====================================================

    if st.button(
        "🚀 Start Learning",
        use_container_width=True
    ):

        st.switch_page("pages/learning.py")
