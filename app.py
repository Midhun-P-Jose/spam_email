import streamlit as st
import joblib

# Set professional page configuration
st.set_page_config(
    page_title="Email Guard | Smart Spam Detection",
    page_icon="🛡️",
    layout="centered"
)

# Load assets
model = joblib.load("svm_spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/shield.png", width=80)
    st.title("Email Guard")
    st.info("Our AI analyzes patterns in text to determine if a message is safe or suspicious.")
    st.write("---")
    st.caption("v1.0.2 | Powered by Smart Classification")

# --- Main Content ---
st.title("🛡️ Email Security Scanner")
st.write("Protect yourself from phishing and unwanted messages. Paste the email content below to scan for security threats.")

# Input area
email_content = st.text_area("Email content to scan", placeholder="Paste your email here...", height=250)

# Execution
if st.button("Scan Message"):
    if not email_content.strip():
        st.warning("⚠️ Please provide content to analyze.")
    else:
        with st.spinner('Analyzing message patterns...'):
            # Transformation and Prediction
            vec = vectorizer.transform([email_content])
            result = model.predict(vec)[0]
        
        # Professional Result Display
        st.subheader("Analysis Result")
        if result == 1:
            st.error("### 🚨 High Risk: Spam Detected")
            st.markdown("""
                **Why was this flagged?**
                * Suspicious urgency or phrasing detected.
                * Pattern matches known unsolicited marketing or phishing styles.
            """)
        else:
            st.success("### ✅ Safe: Legitimate Message")
            st.markdown("This message appears clean and follows standard communication patterns.")

# Footer
st.markdown("---")
st.caption("Disclaimer: This tool is for informational purposes. Always exercise caution with links from unknown senders.")