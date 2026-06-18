# AI Admission Copilot - Retrieval Spike (De-risk Phase)

This directory contains the de-risk retrieval spike for the AI Admission Copilot. The objective of this spike is to quickly prototype, test, and evaluate different chunking strategies, embeddings, and vector database retrieval options to find the most accurate context retrieval configuration.

## Folder Tree

```text
spike/
├── README.md          # Spike documentation and setup guide
├── config.py          # Configuration settings and environment variables
├── evaluation.py      # Module for evaluating retrieval metrics (Hit Rate, MRR)
├── main.py            # Main entry point to run ingestion and evaluation pipeline
├── requirements.txt   # Required python packages
└── retrieval.py       # Module handling document chunking, embedding, and vector search
```

## File Purposes

- **`README.md`**: Provides a high-level overview of the spike, setup instructions, and guidelines for testing/evaluation.
- **`config.py`**: Manages environment variables (API keys, file paths) and stores hyperparameters like chunk size, overlap, embedding models, and target Top-K retrieved documents.
- **`retrieval.py`**: Contains the core logic for the retrieval pipeline, including reading admission documents, applying chunking logic, generating embeddings, indexing chunks in a local vector database (ChromaDB), and searching for candidate documents.
- **`evaluation.py`**: Sets up the evaluation framework. It runs a test set of synthetic or ground-truth queries, compares retrieved contexts against gold-standard targets, and calculates metrics like Hit Rate at K, Mean Reciprocal Rank (MRR), and relevance.
- **`main.py`**: Orchestrates the entire flow from configuration initialization and ingestion to running queries and displaying evaluation reports.
- **`requirements.txt`**: Pinpoints dependencies required for LLM interaction, vector storage, and data evaluation.
