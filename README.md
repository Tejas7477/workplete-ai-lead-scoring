
# Workplete AI Lead Scoring Agent

This is a Streamlit + REST API project that predicts the conversion likelihood of business leads based on features such as company size, industry, and interaction score.

## 🔍 Problem Statement

Build an AI agent that helps Workplete's clients prioritize B2B leads using past lead data.

## 🚀 Features

- Streamlit UI for interactive predictions
- REST API endpoint for programmatic scoring
- Trained classification model
- CSV-based input and preprocessing

## 🧠 Model

Uses RandomForestClassifier trained on features:
- company_size
- industry
- interaction_score
- prior_purchases
- region
## 📽️ Loom Demo

Watch the full working demo 👉 [https://www.loom.com/share/2b2cbe27b05c4d708d51d5bf79f43295}

## 📝 Report (PDF)

Download the detailed report 👉 [https://drive.google.com/file/d/1H3aEoKgNLDt_DTIFVa8t4zeMIqpPIaG1/view?usp=drivesdk]

## 🧠 How it Works

1. User enters lead info via UI
2. Frontend sends data to FastAPI backend
3. Backend uses ML model to return prediction
4. UI displays whether the lead is likely to convert

## 📌 Author

Made  by [Tejas Dhokchaule](https://github.com/Tejas7477)
## 🚀 How to Run This Project Locally

### 1. Clone the Repository
bash
git clone https://github.com/your-username/workplete-ai-agent.git
cd workplete-ai-agent


### 2. Create and Activate Virtual Environment
bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


### 3. Install Dependencies
bash
pip install -r requirements.txt


### 4. Run the Streamlit App
bash
streamlit run app.py

