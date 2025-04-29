import streamlit as st

st.set_page_config(page_title="ConstituLearn", layout="centered")

# Home Page
st.title("🎓 ConstituLearn")
st.subheader("A Free NCERT-Based Learning Platform for Classes 5–10")

st.markdown("""
Welcome to **ConstituLearn**, an interactive web app that helps students learn:

📚 Social Studies  
🏛️ Indian Constitution  
🌍 Geography, History, Civics  
📝 Auto-generated lessons & quizzes  
🎯 Fun gamified learning experience  

### 👨‍🏫 Choose Your Class Below:
""")

class_choice = st.selectbox("Select Class", [
    "Class 5",
    "Class 6",
    "Class 7",
    "Class 8",
    "Class 9",
    "Class 10"
])

st.success(f"You selected: {class_choice}")
st.markdown("---")

st.markdown("📘 Coming soon: Full lessons, quizzes, and badges!")