from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")


class Input(BaseModel):
    text: str


@app.post("/")
def get_sentiment(data: Input):
    result = classifier(data.text)[0]
    return {"label": result["label"], "score": result["score"]}
