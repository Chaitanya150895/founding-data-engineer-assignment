
---

## 📄 `architecture.md`

```markdown
# Architecture Design

## Data Flow
1. **Conversation Ingestion** → Raw chat data ingested into MongoDB.
2. **Embedding Generation** → Sentence-Transformers generate 384-dim embeddings.
3. **Vector Storage** → Embeddings stored in Milvus with metadata.
4. **Graph Mapping** → User-campaign relationships modeled in Neo4j.
5. **Analytics Layer** → Aggregated metrics stored in SQLite (mock for BigQuery).
6. **Caching** → Redis caches recent sessions for latency optimization.

## Orchestration
- **Prefect** used for workflow orchestration (Python DAGs).
- Real-time ingestion flows into MongoDB + Redis.
- Batch aggregation flows into SQLite/BigQuery.

## Scaling & Fault Tolerance
- **Milvus**: HNSW indexing for sub-100ms queries.
- **Neo4j**: Sharding by campaign type.
- **MongoDB**: Replica sets for HA.
- **Redis**: Cluster mode for caching.
- **BigQuery**: Partitioned tables for cost efficiency.
