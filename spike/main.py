"""
Main entry point for running the retrieval spike pipeline.
Orchestrates ingestion, querying, and evaluation.
"""

def main():
    """
    Runs the end-to-end retrieval spike flow:
    1. Load configuration.
    2. Ingest documents.
    3. Run test queries and retrieve context.
    4. Run retrieval evaluation metrics.
    """
    print("Admission Copilot Retrieval Spike Orchestrator")

if __name__ == "__main__":
    main()
