# 🤖 Smart Forecast Deployment API

A FastAPI-based microservice that forecasts future temperature sensor readings using a trained [Prophet](https://facebook.github.io/prophet/) model and flags potential failure risks based on a critical threshold.

This is part of my series on **AI for Predictive Maintenance and Smart Automation**.

---

##  Features

-  Predict future equipment temperatures via REST API
-  Identify timestamps with high failure risk (`> 78°F`)
-  Built using Facebook Prophet
-  Serve predictions using FastAPI
-  Built for production-readiness with Docker (optional)

---

##  Tech Stack

- Python 3.x  
- Facebook Prophet  
- FastAPI  
- Pandas  
- Uvicorn  
- Docker (coming soon)

---

##  How to Run Locally

###  1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/rajkumar160798/smart-forecast-deployment-api.git
cd smart-forecast-deployment-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Train Prophet Model

```
python train_model.py
```

## Launch the FastAPI Server
```
uvicorn app.main:app --reload
```
Navigate to:
📍 http://127.0.0.1:8000/docs
to access the Swagger API UI.

## Sample Request
POST /predict

```json
Copy
Edit
{
  "start_date": "2024-04-01 00:00:00",
  "periods": 48
}
```

## Sample Response:

```json
Copy
Edit
[
  {
    "ds": "2024-04-01 01:00:00",
    "yhat": 72.38,
    "failure_risk": false
  },
  ...
]
```

## Blog Post
Read the full tutorial explaining how this API works:
📘 Coming soon: Deploying AI Forecast Models with FastAPI + Docker

---

## 👨‍💻 Author
**Raj Kumar Myakala**  
AI | Data | Automation | GCP | Python  
[LinkedIn ](https://www.linkedin.com/in/raj-kumar-myakala-927860264/)  
[GitHub ](https://github.com/rajkumar160798)

---

>  If you like this project, consider starring the repo and following my GitHub for more AI/ML innovations!
