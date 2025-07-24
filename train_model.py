import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from utils.preprocess import preprocess_data

def train_and_save_model(csv_path):
    df = pd.read_csv(csv_path)
    X, y, le_industry, le_region = preprocess_data(df)

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, 'data/model.joblib')
    joblib.dump(le_industry, 'data/le_industry.joblib')
    joblib.dump(le_region, 'data/le_region.joblib')
    print("✅ Model and encoders saved!")

if __name__ == "__main__":
    train_and_save_model("data/leads.csv")