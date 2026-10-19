# 📩 SMS / Email Spam Detection System

An end-to-end Machine Learning classification web app built using Python, Scikit-Learn, Natural Language Processing (NLP), and Streamlit. This app classifies incoming messages as Spam or Safe (Ham) in real-time.

---

## 🚀 Live Demo
🔗 https://spam-classifier-k9c8lfrqebsy3qfhvybxnk.streamlit.app/

---

## 📌 Project Features
- **Binary Classification**: Categorizes text messages into Spam (1) or Ham (0).
- **Text Feature Extraction**: Uses `TfidfVectorizer` (Term Frequency-Inverse Document Frequency) to convert raw text into meaningful numerical vectors.
- **Machine Learning Model**: Powered by **Logistic Regression** classifier.
- **Interactive Web UI**: Built with Streamlit for instant user predictions.
- **Cloud Deployment**: Deployed live on Streamlit Community Cloud via GitHub.

---

## 🛠️ Tech Stack & Libraries
- **Language**: Python
- **Machine Learning**: Scikit-Learn
- **Text Processing / NLP**: Pandas, Scikit-Learn TfidfVectorizer
- **Web Framework**: Streamlit
- **Version Control & Hosting**: GitHub, Streamlit Cloud

---

## 📂 Project Structure
```text
├── app.py                  # Streamlit web application interface
├── vectorizer.pkl          # Saved TF-IDF vectorizer model
├── spam_model.pkl          # Trained Logistic Regression classifier model
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation
