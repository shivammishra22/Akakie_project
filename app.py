from fastapi import FastAPI
from api import classify_email

app = FastAPI()

@app.post("/classify")
def classify(input_data: dict):
    return classify_email(input_data["email"])
