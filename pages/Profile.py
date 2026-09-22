import streamlit as st


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Brainbyte Profile",
    page_icon="👤",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

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


# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

/* ==================================================
   BRAINBYTE PROFILE
   Light + Dark Theme
   ================================================== */

.stApp {
    background:
        radial-gradient(
            circle at top left,
            rgba(99, 102, 241, 0.14),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(139, 92, 246, 0.10),
            transparent 35%
        ),
        var(--background-color);
}


/* ---------- Main Container ---------- */

.block-container {
    max-width: 1000px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}


/* ---------- Header ---------- */

.brainbyte-title {
    text-align: center;

    font-size: 46px;
    font-weight: 800;

    letter-spacing: -1px;

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


.brainbyte-subtitle {
    text-align: center;

    font-size: 18px;

    color: var(--text-color);

    opacity: 0.7;

    margin-bottom: 35px;
}


/* ---------- Section Titles ---------- */

.section-title {
    font-size: 23px;
    font-weight: 700;

    color: var(--text-color);

    margin-bottom: 15px;
}


/* ---------- Streamlit Containers ---------- */

[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--secondary-background-color) !important;

    border:
        1px solid rgba(128, 128, 128, 0.22) !important;

    border-radius: 18px !important;

    padding: 22px 24px !important;

    margin-bottom: 20px !important;

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.08) !important;
}


/* ---------- Input Labels ---------- */

label {
    color: var(--text-color) !important;

    font-weight: 600 !important;
}


/* ---------- Inputs ---------- */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background: var(--background-color) !important;

    color: var(--text-color) !important;

    border:
        1px solid rgba(128, 128, 128, 0.30) !important;

    border-radius: 10px !important;
}


/* ---------- Input Focus ---------- */

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color:
        var(--primary-color) !important;

    box-shadow:
        0 0 0 1px var(--primary-color) !important;
}


/* ---------- Selectbox Text ---------- */

.stSelectbox div[data-baseweb="select"] span {
    color: var(--text-color) !important;
}


/* ---------- Buttons ---------- */

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
        0 7px 18px rgba(99, 102, 241, 0.25);

    transition: all 0.2s ease-in-out;
}


/* ---------- Button Hover ---------- */

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 11px 25px rgba(99, 102, 241, 0.35);
}


/* ---------- Profile Summary ---------- */

.profile-summary {
    background: var(--secondary-background-color);

    border:
        1px solid rgba(128, 128, 128, 0.22);

    border-radius: 18px;

    padding: 24px;

    margin-top: 10px;

    color: var(--text-color);

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.08);
}


.profile-summary h3 {
    margin-top: 0;

    margin-bottom: 20px;

    color: var(--text-color);

    font-size: 24px;
}


.profile-summary p {
    color: var(--text-color);

    font-size: 16px;

    line-height: 1.8;

    margin: 7px 0;
}


.profile-summary b {
    color: var(--text-color);
}


/* ---------- Success Message ---------- */

[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ---------- Divider ---------- */

hr {
    border-color:
        rgba(128, 128, 128, 0.25) !important;
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


    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #161b22 !important;

        border-color: #30363d !important;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.35) !important;
    }


    .profile-summary {
        background: #161b22;

        border-color: #30363d;

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.35);
    }


    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div {
        background: #0d1117 !important;

        border-color: #30363d !important;
    }
}


/* ==================================================
   MOBILE
   ================================================== */

@media (max-width: 768px) {

    .brainbyte-title {
        font-size: 36px;
    }

    .brainbyte-subtitle {
        font-size: 16px;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 17px !important;

        border-radius: 14px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

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


# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

with st.container(border=True):

    st.markdown(
        '<div class="section-title">👤 Basic Information</div>',
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
        value=st.session_state.age
    )

    learning_level = st.text_input(
        "Class / Learning Level",
        value=st.session_state.student_class,
        placeholder="Example: BCA, Class 12, Beginner"
    )


# --------------------------------------------------
# SUBJECT
# --------------------------------------------------

with st.container(border=True):

    st.markdown(
        '<div class="section-title">📚 Learning Subject</div>',
        unsafe_allow_html=True
    )

    current_subject = ""

    if st.session_state.subjects:
        current_subject = st.session_state.subjects[0]

    subject_input = st.text_input(
        "Subject",
        value=current_subject,
        placeholder="Example: Physics, Mathematics, Python"
    )


# --------------------------------------------------
# LEARNING GOAL
# --------------------------------------------------

with st.container(border=True):

    st.markdown(
        '<div class="section-title">🎯 Learning Goal</div>',
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


# --------------------------------------------------
# STUDY TIME
# --------------------------------------------------

with st.container(border=True):

    st.markdown(
        '<div class="section-title">⏰ Daily Study Time</div>',
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
        index=study_options.index(current_study_time)
    )


# --------------------------------------------------
# LEARNING STYLE
# --------------------------------------------------

with st.container(border=True):

    st.markdown(
        '<div class="section-title">🧠 Learning Style</div>',
        unsafe_allow_html=True
    )

    learning_style_options = [
        "Simple Explanation",
        "Examples",
        "Step-by-Step",
        "Practice First",
        "Detailed Explanation"
    ]

    current_learning_style = st.session_state.learning_style

    if current_learning_style not in learning_style_options:
        current_learning_style = "Simple Explanation"

    learning_style = st.selectbox(
        "How would you like your AI Tutor to teach you?",
        learning_style_options,
        index=learning_style_options.index(
            current_learning_style
        )
    )


# --------------------------------------------------
# SAVE PROFILE
# --------------------------------------------------

st.markdown("---")

if st.button(
    "💾 Save Profile",
    use_container_width=True,
    type="primary"
):

    if name.strip() == "":
        st.error("Please enter your name.")

    elif learning_level.strip() == "":
        st.error("Please enter your class or learning level.")

    elif subject_input.strip() == "":
        st.error("Please enter a subject.")

    else:

        st.session_state.student_name = name.strip()

        st.session_state.age = age

        st.session_state.student_class = (
            learning_level.strip()
        )

        st.session_state.subjects = [
            subject_input.strip()
        ]

        st.session_state.goal = goal

        st.session_state.study_time = study_time

        st.session_state.learning_style = (
            learning_style
        )

        st.session_state.profile_created = True

        # Used by other pages if needed
        st.session_state.selected_subject = (
            subject_input.strip()
        )

        st.success(
            "✅ Your profile has been saved successfully!"
        )


# --------------------------------------------------
# PROFILE SUMMARY
# --------------------------------------------------

if st.session_state.profile_created:

    st.markdown("---")

    st.markdown(
        "### 📋 Your Profile"
    )

    subject_display = (
        st.session_state.subjects[0]
        if st.session_state.subjects
        else "Not specified"
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
                {subject_display}
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


# --------------------------------------------------
# START LEARNING
# --------------------------------------------------

if st.session_state.profile_created:

    st.markdown("---")

    if st.button(
        "🚀 Start Learning",
        use_container_width=True,
        type="primary"
    ):
        st.switch_page("pages/learning.py")
