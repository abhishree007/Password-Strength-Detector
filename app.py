import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def get_suggestions(password):
    suggestions = []
    if len(password) < 8: suggestions.append("❌ Increase length to at least 8 characters.")
    if not re.search(r"[A-Z]", password): suggestions.append("❌ Add an uppercase letter.")
    if not re.search(r"\d", password): suggestions.append("❌ Add a number.")
    if not re.search(r"[!@#$%^&*]", password): suggestions.append("❌ Add a special character.")
    return suggestions

# --- UI SETTINGS ---
st.set_page_config(page_title="AI Shield", page_icon="🛡️", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* 1. Deep Midnight Navy Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #020617, #0f172a, #1e1b4b, #020617);
        background-size: 400% 400%;
        animation: gradient 8s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. Massive Floating Title with Glow */
    @keyframes float {
        0% { transform: translateY(0px); text-shadow: 0 0 20px rgba(56, 189, 248, 0.7); }
        50% { transform: translateY(-20px); text-shadow: 0 0 50px rgba(56, 189, 248, 1); }
        100% { transform: translateY(0px); text-shadow: 0 0 20px rgba(56, 189, 248, 0.7); }
    }
    
    .glow-text {
        color: #38bdf8 !important;
        font-family: 'Inter', sans-serif;
        font-weight: 900 !important;
        font-size: 5rem !important;
        text-align: center;
        animation: float 3s ease-in-out infinite;
        margin-top: 60px;
        margin-bottom: 60px;
        display: block;
        width: 100%;
    }

    /* 3. Sidebar Glassmorphism */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95) !important;
        backdrop-filter: blur(15px);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Model Details")
    st.info("**Algorithm:** Random Forest")
    st.info("**Accuracy:** 95.2%")
    st.write("---")
    st.markdown("### Developer")
    st.success("Abhishree Raj")

# Main Page Header
st.markdown('<p class="glow-text">🛡️ AI Password Shield</p>', unsafe_allow_html=True)

# Reverted to default Streamlit input styling
user_password = st.text_input("Enter a password to test:", type="password")

if st.button("Analyze Security"):
    if user_password:
        vector_input = vectorizer.transform([user_password])
        prediction = model.predict(vector_input)[0]
        
        if prediction == 0:
            st.error("### Strength: WEAK")
            st.progress(33)
            with st.expander("⚠️ Security Fixes"):
                for s in get_suggestions(user_password): st.write(s)
                
        elif prediction == 1:
            st.warning("### Strength: MEDIUM")
            st.progress(66)
            with st.expander("💡 Recommendations"):
                remaining = get_suggestions(user_password)
                for s in remaining: st.write(s)
        else:
            st.success("### Strength: STRONG")
            st.progress(100)
            st.snow()
            st.markdown("✅ **Excellent!** This password follows high-security standards.")
    else:
        st.warning("Please enter a password first!")