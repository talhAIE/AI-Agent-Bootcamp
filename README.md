# AI Agent Bootcamp

A practical collection of notebooks and examples for learning how to build LLM applications, retrieval workflows, and conversational AI with Python and LangChain.

## Overview

This repository documents a hands-on path from Pydantic data models to LangChain components, vector databases, LCEL chains, and chatbots with conversation history. Each folder focuses on one concept and includes runnable examples or supporting resources.

## Features

- Pydantic model and nested-model examples
- Document loading and text-splitting workflows
- OpenAI and Hugging Face embeddings
- Similarity search and retrieval with FAISS and Chroma
- LangChain prompts, output parsers, and reusable chains
- A simple LCEL translation API served with FastAPI and LangServe
- Chatbot examples with message-history management

## Technologies

- Python
- LangChain and LangChain Community
- OpenAI, Groq, and Hugging Face integrations
- FAISS and Chroma vector stores
- Pydantic, FastAPI, LangServe, and Jupyter notebooks

## Installation

1. Clone the repository and open its directory.
2. Create and activate a virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add the API keys required by the notebook or application you want to run to a `.env` file. For example, the LCEL server requires `GROQ_API_KEY`.
5. Open any `.ipynb` file in Jupyter, or start the sample API:

   ```bash
   python 04_Basic_LLM_APP_LCEL/server.py
   ```

## Results

By working through the examples, you can build a complete retrieval pipeline—from loading documents and generating embeddings to storing, searching, and retrieving relevant context. The repository also demonstrates how to compose an LLM chain and expose it as a simple API, plus how to preserve conversation history in a chatbot.

## Future Improvements

- Add clear learning objectives and prerequisites for each module
- Include a sample `.env.example` and setup notes for each provider
- Add tests and example requests for the FastAPI service
- Build an end-to-end RAG application that combines retrieval and chat history
