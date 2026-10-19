import streamlit as st
import pickle

# Load Models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('spam_model.pkl', 'rb'))

st.title("📩 SMS / Email Spam Detection App")
st.write("Enter a message below to check whether it is Spam or Normal:")

user_input = st.text_area("Enter Message Text:")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        # Transform and Predict
        vector_input = tfidf.transform([user_input])
        result = model.predict(vector_input)[0]
        
        if result == 1:
            st.error("🚨 This is a SPAM message!")
        else:
            st.success("✅ This is a Safe (Ham) message!")