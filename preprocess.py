import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()
    le_industry = LabelEncoder()
    le_region = LabelEncoder()

    df['industry'] = le_industry.fit_transform(df['industry'])
    df['region'] = le_region.fit_transform(df['region'])

    features = ['company_size', 'industry', 'interaction_score', 'prior_purchases', 'region']
    X = df[features]
    y = df['converted']

    return X, y, le_industry, le_region