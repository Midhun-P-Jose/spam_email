import streamlit as st
import joblib

model = joblib.load("svm_spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("📧 Spam Email Detector (SVM)")

email = st.text_area("Enter email content", height=200)

if st.button("Predict"):
    if email.strip() == "":
        st.warning("Please enter an email.")
    else:
        email_vec = vectorizer.transform([email])
        prediction = model.predict(email_vec)[0]

        if prediction == 1:
            st.error("🚨 SPAM EMAIL")
        else:
            st.success("✅ NOT SPAM (HAM)")
