import spacy
import requests

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

nlp = spacy.load("en_core_web_sm")


class Input(BaseModel):
    text: str


def get_sentiment(text: str):
    response = requests.post("http://server2", json={"text": text})
    # response = requests.post("http://localhost:5001", json={"text": text})
    return response.json()


@app.post("/analyze_paragraph/")
def analyze_paragraph(data: Input):
    print(f"TEXT:::: {data.text}")
    doc = nlp(data.text)
    sentences = [sent.text for sent in doc.sents]

    results = [get_sentiment(sentence) for sentence in sentences]

    positive_scores = [res["score"] for res in results if res["label"] == "POSITIVE"]
    negative_scores = [res["score"] for res in results if res["label"] == "NEGATIVE"]

    if sum(positive_scores) > sum(negative_scores):
        return {"label": "POSITIVE", "score": sum(positive_scores) / len(sentences)}
    else:
        return {"label": "NEGATIVE", "score": sum(negative_scores) / len(sentences)}
