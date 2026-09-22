import streamlit as st


# ============================================================
# PAGE CONFIGURATION
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

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN APP
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
       MAIN CONTENT WIDTH
       ======================================================== */

    .block-container {
        max-width: 1000px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* ========================================================
       PAGE TITLE
       ======================================================== */

    .profile-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        letter-spacing: -1px;

        background: linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 5px;
    }


    .profile-subtitle {
        text-align: center;
        font-size: 18px;
        color: var(--text-color);
        opacity: 0.70;
        margin-bottom: 35px;
    }


    /* ========================================================
       SECTION CARDS
       ======================================================== */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--secondary-background-color) !important;

        border: 1px solid rgba(128, 128, 128, 0.22) !important;

        border-radius: 18px !important;

        padding: 22px 24px !important;

        margin-bottom: 20px !important;

        box-shadow:
            0 6px 20px rgba(0, 0, 0, 0.07) !important;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 15px;
    }


    /* ========================================================
       INPUTS
       ======================================================== */

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


    /* ========================================================
       SELECT BOX
       ======================================================== */

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


    /* ========================================================
       LABELS
       ======================================================== */

    label {
        color: var(--text-color) !important;
        font-weight: 600 !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {
        width: 100%;

        min-height: 50px;

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
            0 7px 18px rgba(
                99,
                102,
                241,
                0.25
            );

        transition: all 0.2s ease-in-out;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 11px 25px rgba(
                99,
                102,
                241,
                0.35
            );
    }


    /* ========================================================
       PROFILE SUMMARY CARD
       ======================================================== */

    .profile-summary {
        background: var(--secondary-background-color);

        border: 1px solid rgba(
            128,
            128,
            128,
            0.22
        );

        border-radius: 18px;

        padding: 25px;

        margin-top: 10px;

        color: var(--text-color);

        box-shadow:
            0 6px 20px rgba(
                0,
                0,
                0,
                0.07
            );
    }


    .profile-summary-name {
        font-size: 24px;
        font-weight: 700;

        color: var(--text-color);

        margin-bottom: 20px;
    }


    .profile-row {
        padding: 10px 0;

        border-bottom:
            1px solid rgba(
                128,
                128,
                128,
                0.15
            );

        font-size: 16px;

        color: var(--text-color);
    }


    .profile-row:last-child {
        border-bottom: none;
    }


    .profile-label {
        font-weight: 700;
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


        .profile-summary {
            background: #161b22;

            border-color: #30363d;

            box-shadow:
                0 8px 25px rgba(
                    0,
                    0,
                    0,
                    0.35
                );
        }


        .stTextInput input,
        .stNumberInput input,
        .stSelectbox div[data-baseweb="select"] > div {
            background: #0d1117 !important;

            border-color: #30363d !important;
        }
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .profile-title {
            font-size: 36px;
        }

        .profile-subtitle {
            font-size: 16px;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            padding: 17px !important;
            border-radius: 14px !important;
        }

        .profile-summary {
            padding: 20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="profile-title">🧠 BrainByte</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="profile-subtitle">'
    'Create your personal learning profile'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# BASIC INFORMATION
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-title">'
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
        '<div class="section-title">'
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
        '<div class="section-title">'
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
        '<div class="section-title">'
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
        '<div class="section-title">'
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
        st.error("Please enter a subject.")

    else:

        st.session_state.student_name = (
            name.strip()
        )

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

        st.session_state.study_time = (
            study_time
        )

        st.session_state.learning_style = (
            learning_style
        )

        st.session_state.profile_created = True

        st.success(
            "✅ Your profile has been saved successfully!"
        )


# ============================================================
# PROFILE SUMMARY
# ============================================================

if st.session_state.profile_created:

    st.markdown("---")

    st.markdown("### 📋 Your Profile")

    if st.session_state.subjects:
        subject_display = (
            st.session_state.subjects[0]
        )
    else:
        subject_display = "Not specified"

    # IMPORTANT:
    # This is a normal HTML div rendered with
    # st.markdown().
    #
    # It is NOT st.code() and NOT st.write().
    #
    # Therefore the HTML tags will NOT appear
    # as visible code on the page.

    st.markdown(
        f"""
        <div class="profile-summary">

            <div class="profile-summary-name">
                👋 Welcome, {st.session_state.student_name}!
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Age:
                </span>
                {st.session_state.age}
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Class / Learning Level:
                </span>
                {st.session_state.student_class}
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Subject:
                </span>
                {subject_display}
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Learning Goal:
                </span>
                {st.session_state.goal}
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Daily Study Time:
                </span>
                {st.session_state.study_time}
            </div>

            <div class="profile-row">
                <span class="profile-label">
                    Learning Style:
                </span>
                {st.session_state.learning_style}
            </div>

        </div>
        """,
        unsafe_allow_html=True
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
        st.switch_page("pages/learning.py")
