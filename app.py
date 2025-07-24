import streamlit as st
import speech_recognition as sr
from utils.predict import score_lead

st.set_page_config(page_title="Lead Scoring Agent", layout="centered")
st.title("🤖 Workplete AI - Lead Scoring Agent")
st.markdown("Predict whether a logistics lead will convert using AI.")

# Input fields
company_size = st.slider("Company Size (Number of Employees)", 1, 1000, 100)
industry = st.selectbox("Industry", ["Freight", "Warehousing", "Trucking", "Shipping"])
interaction_score = st.slider("Interaction Score", 0, 100, 50)
prior_purchases = st.slider("Number of Prior Purchases", 0, 10, 0)
region = st.selectbox("Region", ["North", "South", "East", "West", "Central"])

# --- VOICE INPUT SECTION ---
st.markdown("🎤 *Or use voice input* (say: 100 Freight 85 3 West)")

if st.button("🎙️ Voice Input"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please say: 100 Freight 85 3 West")
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        speech_text = recognizer.recognize_google(audio)
        st.success(f"📢 You said: {speech_text}")

        parts = speech_text.split()
        if len(parts) != 5:
            st.error("Please say exactly 5 values in the format: size industry score purchases region.")
        else:
            company_size = int(parts[0])
            industry = parts[1].capitalize()
            interaction_score = int(parts[2])
            prior_purchases = int(parts[3])
            region = parts[4].capitalize()

            pred, prob = score_lead(company_size, industry, interaction_score, prior_purchases, region)
            st.success(f"🎯 Prediction: {'✅ Converted' if pred == 1 else '❌ Not Converted'}")
            st.info(f"📊 Confidence: {prob * 100:.2f}%")

    except sr.UnknownValueError:
        st.error("Speech could not be understood. Try again.")
    except sr.RequestError as e:
        st.error(f"Speech recognition error: {e}")
    except Exception as e:
        st.error(f"Error processing input: {e}")

# --- MANUAL BUTTON ---
if st.button("Score Lead (Manual Input)"):
    pred, prob = score_lead(company_size, industry, interaction_score, prior_purchases, region)
    st.success(f"🎯 Prediction: {'✅ Converted' if pred == 1 else '❌ Not Converted'}")
    st.info(f"📊 Confidence: {prob * 100:.2f}%")