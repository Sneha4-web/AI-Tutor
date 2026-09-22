import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Brainbyte Profile",
    page_icon="👤",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "student_name" not in st.session_state:
    st.session_state.student_name = ""

if "age" not in st.session_state:
    st.session_state.age = 18

if "student_class" not in st.session_state:
    st.session_state.student_class = ""

if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "goal" not in st.session_state:
    st.session_state.goal = "Understand Concepts"

if "study_time" not in st.session_state:
    st.session_state.study_time = "15 minutes"

if "learning_style" not in st.session_state:
    st.session_state.learning_style = "Simple Explanation"

if "profile_created" not in st.session_state:
    st.session_state.profile_created = False

if "selected_subject" not in st.session_state:
    st.session_state.selected_subject = ""


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   MAIN BACKGROUND
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99, 102, 241, 0.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(139, 92, 246, 0.10),
            transparent 30%
        ),
        var(--background-color);
}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

.block-container {
    max-width: 1000px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* ============================================================
   TITLE
   ============================================================ */

h1 {
    text-align: center !important;

    font-size: 46px !important;

    font-weight: 800 !important;

    letter-spacing: -1px;

    margin-bottom: 5px !important;

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


.profile-subtitle {
    text-align: center;

    color: var(--text-color);

    opacity: 0.70;

    font-size: 18px;

    margin-bottom: 35px;
}


/* ============================================================
   REAL STREAMLIT CONTAINERS
   This prevents the blank/black/white spaces problem.
   ============================================================ */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--secondary-background-color) !important;

    border: 1px solid rgba(
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


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-heading {
    font-size: 21px;

    font-weight: 700;

    color: var(--text-color);

    margin-bottom: 15px;
}


/* ============================================================
   INPUTS
   ============================================================ */

.stTextInput input,
.stNumberInput input {
    background: var(--background-color) !important;

    color: var(--text-color) !important;

    border: 1px solid rgba(
        128,
        128,
        128,
        0.30
    ) !important;

    border-radius: 10px !important;
}


/* ============================================================
   SELECT BOX
   ============================================================ */

.stSelectbox div[data-baseweb="select"] > div {
    background: var(--background-color) !important;

    color: var(--text-color) !important;

    border: 1px solid rgba(
        128,
        128,
        128,
        0.30
    ) !important;

    border-radius: 10px !important;
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

label {
    color: var(--text-color) !important;

    font-weight: 600 !important;
}


/* ============================================================
   BUTTONS
   ============================================================ */

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


/* ============================================================
   PROFILE SUMMARY
   ============================================================ */

.profile-summary-title {
    font-size: 24px;

    font-weight: 750;

    color: var(--text-color);

    margin-bottom: 5px;
}


.profile-summary-subtitle {
    color: var(--text-color);

    opacity: 0.65;

    margin-bottom: 20px;
}


/* ============================================================
   PROFILE INFORMATION BOXES
   ============================================================ */

.profile-info-box {
    background: var(--background-color);

    border: 1px solid rgba(
        128,
        128,
        128,
        0.18
    );

    border-radius: 14px;

    padding: 14px 16px;

    margin-bottom: 10px;
}


/* ============================================================
   DARK MODE
   ============================================================ */

@media (prefers-color-scheme: dark) {

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(
                    99,
                    102,
                    241,
                    0.18
                ),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 90%,
                rgba(
                    139,
                    92,
                    246,
                    0.15
                ),
                transparent 30%
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


    .profile-info-box {
        background: #0e1117;

        border-color: #30363d;
    }


    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background: #0e1117 !important;

        border-color: #30363d !important;
    }
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {
        padding-top: 2rem;

        padding-left: 1rem;

        padding-right: 1rem;
    }


    h1 {
        font-size: 36px !important;
    }


    .profile-subtitle {
        font-size: 16px;
    }


    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 17px !important;

        border-radius: 14px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("👤 Your Profile")

st.markdown(
    '<div class="profile-subtitle">'
    'Create your profile to personalize your BrainByte learning experience.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# BASIC INFORMATION
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-heading">'
        '👤 Basic Information'
        '</div>',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "Your Name",
        value=st.session_state.student_name,
        placeholder="Enter your name"
    )

    age = st.number_input(
        "Age",
        min_value=5,
        max_value=100,
        value=st.session_state.age,
        step=1
    )

    learning_level = st.text_input(
        "Class / Learning Level",
        value=st.session_state.student_class,
        placeholder="Example: BCA, College, Class 12"
    )


# ============================================================
# SUBJECT
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-heading">'
        '📚 Learning Subject'
        '</div>',
        unsafe_allow_html=True
    )

    current_subject = ""

    if st.session_state.subjects:
        current_subject = st.session_state.subjects[0]

    subject_input = st.text_input(
        "Subject",
        value=current_subject,
        placeholder="Example: Physics, Data Structure, Python"
    )


# ============================================================
# LEARNING GOAL
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-heading">'
        '🎯 Learning Goal'
        '</div>',
        unsafe_allow_html=True
    )

    goal_options = [
        "Understand Concepts",
        "Prepare for Exams",
        "Practice Questions",
        "Improve Weak Areas",
        "Learn from Basics"
    ]

    current_goal = st.session_state.goal

    if current_goal not in goal_options:
        current_goal = "Understand Concepts"

    goal = st.selectbox(
        "What do you want to achieve?",
        goal_options,
        index=goal_options.index(current_goal)
    )


# ============================================================
# DAILY STUDY TIME
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-heading">'
        '⏰ Daily Study Time'
        '</div>',
        unsafe_allow_html=True
    )

    study_options = [
        "15 minutes",
        "30 minutes",
        "45 minutes",
        "1 hour",
        "2 hours"
    ]

    current_study_time = st.session_state.study_time

    if current_study_time not in study_options:
        current_study_time = "15 minutes"

    study_time = st.selectbox(
        "How much time can you study each day?",
        study_options,
        index=study_options.index(
            current_study_time
        )
    )


# ============================================================
# LEARNING STYLE
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-heading">'
        '🧠 Learning Style'
        '</div>',
        unsafe_allow_html=True
    )

    learning_style_options = [
        "Simple Explanation",
        "Examples",
        "Step-by-Step",
        "Practice First",
        "Detailed Explanation"
    ]

    current_learning_style = (
        st.session_state.learning_style
    )

    if current_learning_style not in learning_style_options:
        current_learning_style = "Simple Explanation"

    learning_style = st.selectbox(
        "How would you like your AI Tutor to teach you?",
        learning_style_options,
        index=learning_style_options.index(
            current_learning_style
        )
    )


# ============================================================
# SAVE PROFILE
# ============================================================

st.markdown("---")

if st.button(
    "💾 Save Profile",
    use_container_width=True,
    type="primary"
):

    if name.strip() == "":
        st.error("Please enter your name.")

    elif learning_level.strip() == "":
        st.error(
            "Please enter your class or learning level."
        )

    elif subject_input.strip() == "":
        st.error(
            "Please enter a subject."
        )

    else:

        st.session_state.student_name = name.strip()

        st.session_state.age = age

        st.session_state.student_class = (
            learning_level.strip()
        )

        st.session_state.subjects = [
            subject_input.strip()
        ]

        st.session_state.selected_subject = (
            subject_input.strip()
        )

        st.session_state.goal = goal

        st.session_state.study_time = study_time

        st.session_state.learning_style = (
            learning_style
        )

        st.session_state.profile_created = True

        st.success(
            "✅ Your profile has been saved successfully!"
        )


# ============================================================
# SAVED PROFILE
# ============================================================

if st.session_state.profile_created:

    st.markdown("---")

    # IMPORTANT:
    # The saved profile uses ONLY normal Streamlit widgets.
    # There is NO HTML here.
    # Therefore <h3>, <p>, <b>, etc. CANNOT appear.

    with st.container(border=True):

        st.markdown(
            "### 📋 Your Profile"
        )

        st.caption(
            f"Welcome back, {st.session_state.student_name}! "
            "Your personalized learning profile is ready."
        )

        # ----------------------------------------------------
        # ROW 1
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "#### 👤 Name"
            )

            st.info(
                st.session_state.student_name
            )

        with col2:

            st.markdown(
                "#### 🎂 Age"
            )

            st.info(
                str(st.session_state.age)
            )

        # ----------------------------------------------------
        # ROW 2
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "#### 🎓 Class / Learning Level"
            )

            st.info(
                st.session_state.student_class
            )

        with col2:

            subject_display = (
                st.session_state.subjects[0]
                if st.session_state.subjects
                else "Not specified"
            )

            st.markdown(
                "#### 📚 Subject"
            )

            st.info(
                subject_display
            )

        # ----------------------------------------------------
        # ROW 3
        # ----------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "#### 🎯 Learning Goal"
            )

            st.info(
                st.session_state.goal
            )

        with col2:

            st.markdown(
                "#### ⏰ Daily Study Time"
            )

            st.info(
                st.session_state.study_time
            )

        # ----------------------------------------------------
        # ROW 4
        # ----------------------------------------------------

        st.markdown(
            "#### 🧠 Learning Style"
        )

        st.info(
            st.session_state.learning_style
        )


# ============================================================
# START LEARNING
# ============================================================

if st.session_state.profile_created:

    st.markdown("---")

    if st.button(
        "🚀 Start Learning",
        use_container_width=True,
        type="primary"
    ):
        st.switch_page(
            "pages/learning.py"
        )
