import streamlit as st
import joblib
import re

# Load saved model and vectorizer
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def get_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("❌ Increase length to at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("❌ Add at least one uppercase letter (A-Z).")
    if not re.search(r"[a-z]", password):
        suggestions.append("❌ Add at least one lowercase letter (a-z).")
    if not re.search(r"\d", password):
        suggestions.append("❌ Add at least one numeric digit (0-9).")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("❌ Add at least one special character (!@#$%).")
    return suggestions

st.set_page_config(page_title="AI Password Analyzer", page_icon="🔐")
st.title("🔐 AI-Based Password Strength Detector")

user_password = st.text_input("Enter a password to test:", type="password")

if st.button("Check Strength"):
    if user_password:
        vector_input = vectorizer.transform([user_password])
        prediction = model.predict(vector_input)[0]
        
        if prediction == 0:
            st.error("Strength: **WEAK**")
            st.subheader("How to improve:")
            for s in get_suggestions(user_password):
                st.write(s)
        elif prediction == 1:
            st.info("Strength: **MEDIUM**")
            st.subheader("Recommendations:")
            remaining = get_suggestions(user_password)
            if not remaining:
                st.write("💡 Your password has the right parts, but try making it longer or more random!")
            else:
                for s in remaining:
                    st.write(s)
        else:
            st.success("Strength: **STRONG**")
            st.balloons()
    else:
        st.warning("Please enter a password first!")