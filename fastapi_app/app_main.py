import asyncio
import os
import pickle

import dagshub
import mlflow
import mlflow.pyfunc

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from text_processing import normalize_text


## Use it when you want run the "app.py" in a local enviorment
## like (mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000

# mlflow.set_tracking_uri("https://dagshub.com/pranay-majumder/Docker_Pipeline_CI_CD.mlflow")
# dagshub.init(repo_owner="pranay-majumder", repo_name="Docker_Pipeline_CI_CD", mlflow=True)


# ============================================================
# MLflow + DagsHub configuration
# ============================================================

dagshub_token = os.getenv("DAGSHUB_TOKEN")

if not dagshub_token:
    raise EnvironmentError("DAGSHUB_TOKEN environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "pranay-majumder"
repo_name = "Docker_Pipeline_CI_CD"

mlflow.set_tracking_uri(
    f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow"
)


# ============================================================
# FastAPI application
# ============================================================

app = FastAPI(
    title="Sentiment Analysis API",
    description="Sentiment Analysis using BoW + Logistic Regression",
    version="1.0.0"
)


# ============================================================
# Request schema
# ============================================================

class TextRequest(BaseModel):
    text: str


# ============================================================
# Load BoW vectorizer
# ============================================================

with open("./models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# ============================================================
# Load Champion model from MLflow Model Registry
# ============================================================

model_name = "Sentiment_Analysis_BoW_LR"

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}@champion"
)


# ============================================================
# Synchronous ML prediction pipeline
# ============================================================

def run_prediction(text: str):
    """
    Complete synchronous prediction pipeline.

    This function is executed inside a thread using
    asyncio.to_thread() so that the FastAPI event loop
    is not blocked.
    """

    # Text preprocessing
    processed_text = normalize_text(text)

    # Text -> BoW features
    features = vectorizer.transform([processed_text])

    # BoW -> Logistic Regression -> prediction
    prediction = model.predict(features)

    return processed_text, prediction


# ============================================================
# Prediction endpoint
# ============================================================

@app.post("/predict")
async def predict(request: TextRequest):

    try:
        # Run the complete synchronous ML pipeline
        # in a thread instead of blocking the event loop.
        processed_text, prediction = await asyncio.to_thread(
            run_prediction,
            request.text
        )

        # happiness = 1, sadness = 0
        sentiment = "happy" if prediction[0] == 1 else "sad"

        return {
            "text": request.text,
            "processed_text": processed_text,
            "sentiment": sentiment
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )