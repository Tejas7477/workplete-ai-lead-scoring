import joblib
import numpy as np

# Load trained model and encoders
model = joblib.load('data/model.joblib')
le_industry = joblib.load('data/le_industry.joblib')
le_region = joblib.load('data/le_region.joblib')

def score_lead(company_size, industry, interaction_score, prior_purchases, region):
    industry_encoded = le_industry.transform([industry])[0]
    region_encoded = le_region.transform([region])[0]

    features = np.array([[company_size, industry_encoded, interaction_score, prior_purchases, region_encoded]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return prediction, probability