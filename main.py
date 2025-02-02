from fastapi import FastAPI
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

# API Endpoints
QUIZ_DATA_URL = "https://api.jsonserve.com/rJvd7g"
HISTORICAL_DATA_URL = "https://api.jsonserve.com/XgAgFJ"
COLLEGE_DATA_URL = "https://api.jsonserve.com/LLQT"

# Fetch data
def fetch_data(url):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Load data
def load_data():
    current_quiz_data = fetch_data(QUIZ_DATA_URL)
    historical_data = fetch_data(HISTORICAL_DATA_URL)
    college_data = fetch_data(COLLEGE_DATA_URL)
    return current_quiz_data, historical_data, college_data

# Analyze performance
def analyze_performance(historical_data, current_quiz_data):
    df = pd.DataFrame(historical_data)
    df['avg_score'] = df['scores'].apply(np.mean)
    
    # Identify weak areas
    topic_accuracy = {}
    for entry in historical_data:
        for question_id, selected_option in entry['response_map'].items():
            topic = entry['topics'][question_id]
            if topic not in topic_accuracy:
                topic_accuracy[topic] = []
            topic_accuracy[topic].append(selected_option == entry['correct_answers'][question_id])
    
    topic_performance = {topic: np.mean(scores) for topic, scores in topic_accuracy.items()}
    
    return df[['user_id', 'avg_score']], topic_performance

# Predict NEET Rank
def predict_rank(performance_df):
    past_neet_data = pd.DataFrame({
        "avg_score": [400, 450, 500, 550, 600, 650, 700],
        "neet_rank": [50000, 40000, 30000, 20000, 10000, 5000, 1000]
    })
    
    model = LinearRegression()
    model.fit(past_neet_data[['avg_score']], past_neet_data['neet_rank'])
    
    performance_df['predicted_rank'] = model.predict(performance_df[['avg_score']])
    return performance_df[['user_id', 'predicted_rank']]

# Predict College
def predict_college(rank_predictions, college_data):
    college_df = pd.DataFrame(college_data)
    
    def get_college(rank):
        return college_df.loc[(college_df['min_rank'] <= rank) & (college_df['max_rank'] >= rank), 'college_name'].values[0] if not college_df.empty else "No college found"
    
    rank_predictions['predicted_college'] = rank_predictions['predicted_rank'].apply(get_college)
    return rank_predictions

@app.get("/predict-rank-college")
def predict():
    current_quiz_data, historical_data, college_data = load_data()
    if not historical_data or not college_data or not current_quiz_data:
        return {"error": "Failed to fetch necessary data"}
    
    performance_df, topic_performance = analyze_performance(historical_data, current_quiz_data)
    rank_predictions = predict_rank(performance_df)
    final_predictions = predict_college(rank_predictions, college_data)
    
    return {
        "rank_predictions": final_predictions.to_dict(orient='records'),
        "topic_performance": topic_performance
    }
