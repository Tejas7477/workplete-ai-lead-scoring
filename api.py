from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model and encoders from the 'data' folder
model = joblib.load("data/model.joblib")
le_industry = joblib.load("data/le_industry.joblib")
le_region = joblib.load("data/le_region.joblib")

# Initialize FastAPI app
app = FastAPI()

# Define the request body schema
class LeadData(BaseModel):
    company_size: int
    industry: str
    interaction_score: float
    prior_purchases: int
    region: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Lead Scoring API"}

@app.post("/predict/")
def predict_lead(data: LeadData):
    # Transform categorical fields
    industry_encoded = le_industry.transform([data.industry])[0]
    region_encoded = le_region.transform([data.region])[0]

    # Prepare the feature vector
    X = [[
        data.company_size,
        industry_encoded,
        data.interaction_score,
        data.prior_purchases,
        region_encoded
    ]]

    # Predict
    prediction = model.predict(X)[0]
    return {"converted": bool(prediction)}