import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Page title
st.set_page_config(page_title="Spam Email Detector")

st.title("📧 Spam Email Detector")
st.write("Enter an email or SMS message below to check whether it is Spam or Not Spam.")

# User input
message = st.text_area("Enter your message")

# Predict
if st.button("Detect Spam"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)

        if prediction[0] == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")