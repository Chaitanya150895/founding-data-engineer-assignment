from prefect import flow, task
from utils.logger import logger
from src.pipeline import ingest, embeddings, storage

@task
def ingest_data():
    logger.info("🚀 Starting ingestion...")
    ingest.generate_sample_data(num_records=20)
    logger.info("✅ Ingestion complete.")

@task
def generate_embeddings():
    logger.info("🚀 Generating embeddings...")
    embeddings.generate_embeddings("data/sample_conversations.json")
    logger.info("✅ Embeddings generated.")

@task
def store_all():
    logger.info("🚀 Storing data in multi-DB...")
    storage.store_data("data/conversations_with_embeddings.json")
    logger.info("✅ Data stored successfully.")

@flow(name="Marketing Personalization Pipeline")
def main_pipeline():
    logger.info("📊 Pipeline started.")
    ingest_data()
    generate_embeddings()
    store_all()
    logger.info("🎉 Pipeline finished successfully.")

if __name__ == "__main__":
    main_pipeline()
