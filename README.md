# ELSA Sentiment Analysis Servers

## Architecture Decisions:
1. **FastAPI**: Used for its asynchronous capabilities and speed.
2. **Spacy**: Industry standard for NLP tasks like sentence splitting.
3. **HuggingFace Transformers**: Provides state-of-the-art models for sentiment analysis.

## How to run:

1. Ensure Docker and docker-compose are installed.
2. Clone the repository from `https://github.com/japdubengsub/elsa-challenge`
3. Navigate to the root directory.
4. Run `docker-compose up`.

## Dependencies:
1. Docker
2. Docker Compose

## Public endpoints:
Server 1 (Paragraph Analyzer): `http://localhost:5000/analyze_paragraph/`

Server 1 (Sentence Analyzer - proxy version): `http://localhost:5000/analyze_sentence/`.

Server 2 (Sentence Analyzer - direct connection): `http://localhost:5001/`.

Post a request with the body `{"text": "Your text here"}`.

Example:
```
curl -X 'POST' \
  'http://localhost:5000/analyze_paragraph/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "I love this product. But the customer service was not good."}'
```

## Testing:
Run ` python ./test_service.py`. while `docker-compose up` is running.

