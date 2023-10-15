Tech challenge task
Introduction

Thank you for your interest in the position of senior developer lead at ELSA.

As part of the interview process we ask you to take this challenge and send it to us for review.

The challenge should not take you more than 3-4h to complete, if it takes much more please let us know!
Challenge description

At ELSA, the speech platform is a Kubernetes namespace where a few servers are making API endpoints available to our mobile apps or as an REST-API to external customers.

For this tech challenge we want to simulate this environment and ask you to build 2 docker images, representing 2 independent servers that are started via docker compose. Each of the images is serving one public endpoint and also communicate internally with each other for the necessary operations. For this challenge we propose you to build 2 endpoints that provide the sentiment of a text paragraph. Each of the two servers will perform a specific task and will communicate to each other for needed functionality as follows:

Server 1:

    This server offers a public endpoint that receives a paragraph of text, splits the paragraph into sentences, and returns the overall sentiment as a combination of the per-sentence analysis of all sentences in the paragraph.
    This server will first split the input text paragraph into sentences, then request to the "ML" server (second server) the analysis of sentiment for each sentence, and return the combined sentiment back to the caller. To do sentence splitting, you can use spacy with one of these methods or propose any other method you would prefer.
    Note how the result of the sentiment analysis ML above can return a "positive" or "negative" decision, and a probability from 0 to 1 for each one. Use your own good judgement on how to combine the scores of multiple sentences. You shall return to the user a decision in the same format (see example below).

Server 2 (ML server):

    This server is used to compute the sentiment of a given sentence. This functionality will be used by server 1 and should also be made available to any outside user via a public endpoint. The endpoint receives a single sentence and returns the sentiment of it (label and score).
    Computation of the sentiment can be easily done using huggingFace models using this example or anything else you would like to use.
    The endpoint should return the same format as returned by huggingface, e.g. {"label": "NEGATIVE","score": 0.9996411800384521} 

An end user should be able to call a single IP:port for both endpoints (single sentence and paragraph processing), which should be abstracted from the user (simulating an API gateway).

Please build the above in python and docker, and provide documentation on the architecture decisions and how to run it and use it.

In addition, please add any tests you believe are necessary to ensure the code is well tested.
Deliverables

    The code you implemented
    A readme.md file explaining your solution and what architecture choices you made. We also appreciate well documented code that is easy to understand
    Instructions in the readme on how to run the code in the command line and what dependencies it has.


