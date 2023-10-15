# ELSA Sentiment Analysis Servers

## Architecture Decisions:
1. **FastAPI**: Used for its asynchronous capabilities and speed.
2. **Spacy**: Industry standard for NLP tasks like sentence splitting.
3. **HuggingFace Transformers**: Provides state-of-the-art models for sentiment analysis.

## How to run:

1. Ensure Docker and docker-compose are installed.
2. Clone the repository.
3. Navigate to the root directory.
4. Run `docker-compose up`.

## Dependencies:
1. Docker
2. Docker Compose

## Endpoints:

Server 1 (Paragraph Analyzer): `http://localhost:5000/analyze_paragraph/`
Server 2 (Sentence Analyzer): `http://localhost:5001/`

Post a request with the body {"text": "Your text here"}.

## Testing:
Run `python -m unittest discover`.

