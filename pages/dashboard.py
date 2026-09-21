import streamlit as st
import pandas as pd
import os
from modules.recommendation import generate_next_topic

st.set_page_config(
    page_title="BrainByte Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# DASHBOARD CSS
# -------------------------------

st.markdown("""
<style>

/* Page background */
.stApp {
    background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
}

/* Main container */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Dashboard title */
.dashboard-title {
    text-align: center;
    margin-bottom: 30px;
}

.dashboard-title h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.dashboard-title p {
    font-size: 17px;
    color: #666;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
    border: 1px solid #eeeeee;
}

div[data-testid="stMetricLabel"] {
    font-size: 15px;
}

div[data-testid="stMetricValue"] {
    font-size: 30px;
    font-weight: 800;
}

/* Section headings */
h2, h3 {
    font-weight: 750;
}

/* Information boxes */
.stAlert {
    border-radius: 14px;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

/* Footer */
.dashboard-footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 My Learning Dashboard")

# Find progress file
file_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "progress.csv"
)

# Load progress
if os.path.exists(file_path):
    progress = pd.read_csv(file_path)
else:
    progress = pd.DataFrame()

# No data yet
if progress.empty:
    st.info("No quiz progress yet. Complete a quiz to see your dashboard.")
    st.stop()

# Statistics
total_quizzes = len(progress)

average_score = progress["quiz_score"].mean()

best_score = progress["quiz_score"].max()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Quizzes",
        total_quizzes
    )

with col2:
    st.metric(
        "Average Score",
        f"{average_score:.1f}%"
    )

with col3:
    st.metric(
        "Best Score",
        f"{best_score:.1f}%"
    )

# Subject progress
st.subheader("📚 Subject Progress")

subject_scores = progress.groupby("subject")["quiz_score"].mean()

for subject, score in subject_scores.items():
    st.write(f"**{subject}** — {score:.1f}%")

# Weak topics
st.subheader("🔧 Topics to Improve")

topic_scores = progress.groupby("topic")["quiz_score"].mean()

weak_topics = topic_scores[topic_scores < 60]

if len(weak_topics) == 0:
    st.success("🎉 No major weak topics yet!")
else:
    for topic, score in weak_topics.items():
        st.write(f"🔴 **{topic}** — {score:.1f}%")

# Strong topics
st.subheader("💪 Strong Topics")

strong_topics = topic_scores[topic_scores >= 80]

if len(strong_topics) == 0:
    st.info("Keep practicing to build your strong-topic list.")
else:
    for topic, score in strong_topics.items():
        st.write(f"🟢 **{topic}** — {score:.1f}%")

st.subheader("🤖 AI Next Topic")

student_subject = st.session_state.get("selected_subject", "")
current_topic = st.session_state.get("selected_topic", "")
difficulty = st.session_state.get("selected_difficulty", "Beginner")
latest_score = progress["quiz_score"].iloc[-1]

if student_subject and current_topic:

    if st.button("✨ Recommend My Next Topic", use_container_width=True):

        with st.spinner("🤖 AI is choosing your next topic..."):

            recommendation = generate_next_topic(
                student_subject,
                current_topic,
                difficulty,
                latest_score
            )

        st.info(recommendation)

else:
    st.info("Complete a learning session first to get an AI recommendation.")
