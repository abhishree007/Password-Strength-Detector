# 🔐 AI-Based Password Strength Detector

An end-to-end Machine Learning application that classifies password strength into **Weak**, **Medium**, and **Strong** using a Random Forest Classifier.

## 🚀 Features
* **AI Engine**: Random Forest model reaching **95% accuracy**.
* **Live Analysis**: Real-time password checking via a Streamlit web interface.
* **Smart Suggestions**: Provides actionable feedback (e.g., "Add a special character") using Regex logic.
* **Comparative Research**: Includes experiments with Logistic Regression and Decision Trees.

## 📊 Performance Comparison
| Model | Accuracy |
| :--- | :--- |
| Logistic Regression | 79% |
| Decision Tree | 89% |
| **Random Forest** | **95%** |

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **ML Libraries**: Scikit-learn, Pandas, Joblib
* **Web Framework**: Streamlit
* **Deployment**: Vectorized via TF-IDF (Character-level)

## 📦 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install streamlit scikit-learn pandas joblib`
3. Run the app: `streamlit run app.py`