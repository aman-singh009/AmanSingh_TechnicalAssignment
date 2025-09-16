Scalable Data Pipeline for a Multi-Department Pharmaceutical Company

📌 Overview



This project designs a hybrid data pipeline (Lambda + Kappa) tailored for the pharmaceutical industry, handling 1M → 10M+ records/day across multiple departments.

It ensures real-time insights, governance, compliance, and scalability while supporting both BI dashboards and advanced ML workflows.



📖 Contents



Executive Summary



Business Context \& Requirements



Architecture Overview



Design Pattern Choice (Hybrid)



Data Flow \& Processing Stages



Implementation Strategy



Data Quality \& Error Handling



Monitoring \& Governance



Data Lineage \& Audit Trails



GDPR \& Compliance



Roadmap \& Scalability Outlook



Conclusion



Appendix (Code References)



🏗️ Architecture



The pipeline follows a layered design:



Ingestion → Apache Kafka (6 departmental topics).



Orchestration → Apache Airflow DAGs (per department).



Processing →



Spark/Flink for real-time ERP \& IoT.



Spark SQL/ETL for batch sources (Clinical, Finance, Regulatory, Social).



Storage → Staging → Cleansed (Delta/Hudi) → Presentation (Snowflake/BigQuery/Redshift).



Serving → BI dashboards (Power BI, Tableau), ML feature store, compliance reporting.



Governance → Amundsen/DataHub, OpenLineage, Great Expectations.



⚡ Design Choice: Hybrid (Lambda + Kappa)



Kappa-style (stream-first) → ERP \& IoT (real-time/near real-time).



Lambda-style (batch + stream) → Clinical, Regulatory, Finance, Social (reproducibility, auditability).



Ensures balance between speed and reliability.



🔄 Data Flow (Example: ERP)



ERP system emits JSON → Kafka (erp\_sales).



Kafka persists event → Airflow DAG triggers consumer.



Data written to staging (raw + metadata).



Cleansing: validation, deduplication, pseudonymization.



Curated records stored in Delta tables → Aggregations in presentation layer.



BI/ML systems consume optimized datasets.



🛠️ Tools \& Technologies



Ingestion: Apache Kafka, Debezium (CDC).



Orchestration: Apache Airflow.



Processing: Spark Structured Streaming, Flink, SQL.



Storage: S3/GCS + Delta Lake/Hudi + Snowflake/BigQuery/Redshift.



Governance \& Quality: Great Expectations, OpenLineage, Amundsen.



Monitoring: Prometheus + Grafana, Slack, PagerDuty.



Security: Vault/KMS, TLS, AES-256 encryption.



✅ Features



Handles real-time + batch workloads.



Scales from 1M → 10M+ records/day.



Data Quality Rules: validation, anomaly detection, DLQ with reprocessing.



Governance \& Lineage: end-to-end traceability.



GDPR Compliance: pseudonymization, right-to-be-forgotten, retention policies.



Phased Roadmap: scalable from POC → enterprise-grade ML pipelines.



👤 Author



Aman Singh

