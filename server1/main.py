from asyncio import gather

import httpx
import spacy
from fastapi import FastAPI
from pydantic import BaseModel

ML_SERVER_URL = "http://server2:80/"

app = FastAPI()

nlp = spacy.load("en_core_web_sm")


class Input(BaseModel):
    text: str


async def get_sentiment(text: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(url=ML_SERVER_URL, json={"text": text})

    return response.json()


@app.post("/analyze_paragraph/")
async def analyze_paragraph(data: Input):
    doc = nlp(data.text)

    results = await gather(*(get_sentiment(sentence.text) for sentence in doc.sents))

    positive_scores = sum([res["score"] for res in results if res["label"] == "POSITIVE"])
    negative_scores = sum([res["score"] for res in results if res["label"] == "NEGATIVE"])

    if positive_scores > negative_scores:
        return {"label": "POSITIVE", "score": positive_scores / len(results)}
    else:
        return {"label": "NEGATIVE", "score": negative_scores / len(results)}


@app.post("/analyze_sentence/")
async def analyze_sentence(data: Input):
    response = await get_sentiment(data.text)
    return response
