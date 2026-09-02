import streamlit as st

#page configuration

st.set_page_config(
    page_title=" Student profile",
    page_icon="👨‍🎓",
    layout="wide"

)

#page title

st.title("👨‍🎓Student profile")
st.subheader("Tell us a little about yourself so your AI Tutor can personalize your learning ")

st.markdown("---")

#student Information

st.subheader("📄Basic Information")
col1, col2 = st.columns(2)
with col1:
    name=st.text_input(
        "Full name",
        placeholder="Enter your full name"
    )

    with col2:
     age=st.number_input(
            "Age",
            min_value=10,
            max_value=50,
            value=18
        )

student_class =st.selectbox(
   "select your class",
   [
   "8th",
   "9th",
   "10th",
   "11th",
   "12th",
   "Bachelors-1st year",
   "Bachelors-2nd year",
   "Bachelors-3rd year",
   "Masters-1st year",
   "Masters-2nd year"
   ]

)  

#subjects

st.subheader("📚Subjects")

subjects=st.multiselect(
   "Which subject do you want to learn?",
   [
      "Mathematics",
      "Science",
      "English",
      "Computer Science",
      "Physics",
      "Chemistry",
      "Biology",
      "Geography",
      "History",
      "Others"
      
   ]
)


if "Other" in  subjects:
   other_subject = st.text_input(
      "Enter your subjrct",
      placeholder="e.g.Economics, Psychology,French"
   ) 
#learning goal
st.subheader("🎯learning goal")
goal = st.radio(
    "what is your main learning goal?",
    [
      "school /collrge exam prepration",
      "Board exam prepration",
      "Competitive exam prepration",
      "Conceptual understanding"
      ]
   )

      
 #Study time

st.subheader("⏲Daily study time")

study_time=st.selectbox(
      "How much time can you study daily?",
      [
         "15 minutes",
         "30 minutes",
         "1 hour",
         "More than 1 hour"
      ]
   )

# Learning Preference

st.subheader("🧠 Learning Preference")

learning_style = st.selectbox(
    "How do you prefer lessons to be explained?",
[
        "Simple Explanation",
        "Real-Life Examples",
        "Exam Focused",
        "Detailed Explanation"
]
)

# Save Profile

st.markdown("---")

if st.button("💾 Save My Profile", use_container_width=True):

    if name.strip() == "":
        st.error("❌ Please enter your name.")

    elif len(subjects) == 0:
        st.error("❌ Please select at least one subject.")

    else:

        # Save information in Streamlit session
        st.session_state.student_name = name
        st.session_state.age = age
        st.session_state.student_class = student_class 
        st.session_state.subjects = subjects
        st.session_state.goal = goal
        st.session_state.study_time = study_time
        st.session_state.learning_style =learning_style
        st.session_state.profile_created = True

        st.success("✅ Your profile has been saved!")

        st.balloons()

        # Show saved profile
        st.subheader("🎉 Your Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Class:** {student_class}")
            st.write(f"**Goal:** {goal}")

        with col2:
            st.write(f"**Subjects:** {', '.join(subjects)}")
            st.write(f"**Daily Study Time:** {study_time}")
            st.write(f"**Learning Style:** {learning_style}")      






        
                       

       