# Scaling Plan

## Handling 10M+ Users
- **Sharding** MongoDB collections by user_id.
- **Partitioning** BigQuery tables by date/campaign.
- **Milvus** cluster deployment with GPU acceleration.

## Sub-100ms Vector Queries
- Use **HNSW indexing** in Milvus.
- Pre-compute embeddings for frequent queries.
- Redis caching for hot user sessions.

## Cost Efficiency
- Use **spot instances** for non-critical batch jobs.
- Optimize BigQuery queries with materialized views.
- Monitor compute/storage usage with Grafana dashboards.
- Autoscale Kubernetes pods based on load.

## Observability
- **Prometheus + Grafana** for metrics.
- **Prefect logs** for pipeline monitoring.
- Anomaly detection for missing embeddings or broken relationships.
