# chi-agent

This project is a starter template for a FastAPI application with OpenAI integration and vector database capabilities via `llama-index`.

## Features

- FastAPI server with minimal endpoints.
- Integration with OpenAI API (requires `OPENAI_API_KEY` env variable).
- Basic retrieval augmented generation (RAG) using LlamaIndex.
- Simple scripts to build a vector index and run the server.

## Setup

1. Install the [`uv`](https://github.com/astral-sh/uv) tool and use it with
   Poetry to install dependencies:

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
uv pip install poetry
poetry install
```

2. Set your OpenAI API key environment variable:

```bash
export OPENAI_API_KEY=your_key_here
```

3. Build the index from documents placed in the `data/` directory:

```bash
python scripts/build_index.py
```

4. Start the server:

```bash
./scripts/run_server.sh
```

The server will run on `http://localhost:8000`.

