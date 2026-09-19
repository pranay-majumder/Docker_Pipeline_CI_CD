import pickle
import mlflow
import mlflow.pyfunc
import dagshub
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from text_processing import normalize_text


## Use it when you want run the "app.py" in a local enviorment
## like (mlops_venv) PS D:\MLOPS\Lecture_21_Docker\fastapi_app> uvicorn app:app --reload --port 8000
# mlflow.set_tracking_uri("https://dagshub.com/pranay-majumder/Docker_Pipeline_CI_CD.mlflow")
# dagshub.init(repo_owner="pranay-majumder", repo_name="Docker_Pipeline_CI_CD", mlflow=True)


# MLflow + DagsHub
# Set up DagsHub credentials for MLflow tracking (Usefull for GitHub Actions CI/CD Pipeline)
dagshub_token = os.getenv("DAGSHUB_TOKEN")
if not dagshub_token:
    raise EnvironmentError("DAGSHUB_TOKEN environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "pranay-majumder"
repo_name = "Docker_Pipeline_CI_CD"

# Set up MLflow tracking URI
mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')


app = FastAPI(
    title="Sentiment Analysis API",
    description="Sentiment Analysis using BoW + Logistic Regression",
    version="1.0.0"
)


# Request Schema
class TextRequest(BaseModel):
    text: str


# Load BoW Vectorizer
# with open("../models/vectorizer.pkl", "rb") as file:  ## For Local Use
with open("./models/vectorizer.pkl", "rb") as file:     ## For Docker Use (See Dockerfile and Understand Folder Structure)
    vectorizer = pickle.load(file)


# Load Latest Model (Champion --> Current Model in Production) from MLflow Model Registry
model_name = "Sentiment_Analysis_BoW_LR"

## Here we are loading the model using the model name and specifying the version as "champion" 
## to get the current production model. This allows us to always use the latest registered model 
## for predictions without hardcoding a specific version number.

## 
model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}@champion"
)


@app.post("/predict")
def predict(request: TextRequest):
    try:
        text = request.text

        # Text preprocessing
        processed_text = normalize_text(text)

        # Text → BoW features
        features = vectorizer.transform([processed_text])

        # BoW → Logistic Regression → Prediction
        prediction = model.predict(features)

        # happiness = 1, sadness = 0
        sentiment = "happy" if prediction[0] == 1 else "sad"

        return {
            "text": text,
            "processed_text": processed_text,
            "sentiment": sentiment
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )