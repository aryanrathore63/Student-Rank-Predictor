# Student Rank Predictor

## Overview
The **Student Rank Predictor** is a FastAPI-based backend solution that analyzes NEET quiz performance and predicts student ranks based on historical data. The system also provides insights into weak areas and potential improvements and predicts the most likely college a student could be admitted to based on their rank.

## Features
- Fetches **Current Quiz Data** (latest quiz submission) and **Historical Quiz Data** (past 5 quizzes).
- Analyzes **topic-wise performance trends**.
- Predicts **NEET rank using a Linear Regression model**.
- Provides **most probable college admissions** based on rank.
- RESTful API for fetching predictions and insights.

## Tech Stack
- **Backend:** FastAPI
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Database:** JSON-based API endpoints (Mock Data)
- **Deployment:** Uvicorn

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/aryanrathore63/student-rank-predictor.git
cd student-rank-predictor
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```bash
uvicorn main:app --reload
```

### 5. Test the API
Open in browser:
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Test Predictions: [http://127.0.0.1:8000/predict-rank-college](http://127.0.0.1:8000/predict-rank-college)

## Approach
1. **Data Collection:** Fetch quiz & historical performance data via API endpoints.
2. **Data Analysis:** Identify weak areas, improvement trends, and response accuracy.
3. **Prediction Model:** Use **Linear Regression** to predict NEET rank based on past scores.
4. **College Prediction:** Map predicted ranks to college admission data.
5. **API Integration:** Develop FastAPI endpoints for rank and insights retrieval.

## Screenshots
(Include screenshots of API responses, performance insights, and visualizations here)

## Future Improvements
- Improve accuracy using advanced ML models (Random Forest, XGBoost).
- Store data in a database (PostgreSQL/MySQL) instead of API endpoints.
- Develop a **frontend dashboard** for interactive reports.

---
🚀 **Created by Aryan Rathore** | [LinkedIn](https://linkedin.com/in/aryan-rathore01) | [GitHub](https://github.com/aryanrathore63)

