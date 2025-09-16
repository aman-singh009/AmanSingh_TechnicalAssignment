AWS Cloud Analytics Migration Documentation



📌 Project Overview



Project: Migration of On-Premises Power BI Solution to AWS Cloud

Prepared by: Aman Singh

Date: 15/09/2025



The pharmaceutical company migrated its legacy on-premises Power BI solution to a cloud-native AWS analytics platform to improve scalability, reduce costs, and support regulatory compliance.



The AWS solution replicates existing Power BI functionality while adding automation, cost-efficiency, and integration with advanced services.



🎯 Objectives



Replace on-prem Power BI with AWS-native services.



Maintain equivalent functionality (dashboards, KPIs, reports).



Enhance scalability to handle growing data volumes.



Ensure compliance with HIPAA and pharma regulations.



Reduce infrastructure and maintenance costs.



🏗️ Solution Architecture



The architecture follows a layered data lake + analytics design:



Amazon S3 – Data Lake with Raw → Processed → Presentation zones.



AWS Glue – Serverless ETL for cleaning, transformation, and schema cataloging.



Amazon Athena – SQL queries on partitioned Parquet datasets.



Amazon QuickSight – Cloud-native BI dashboards replacing Power BI.



Security \& Governance – IAM, Row-Level Security (RLS), encryption, CloudTrail auditing.



🔄 Migration Phases

Phase 1: Learning \& Planning



Studied QuickSight features (SPICE, drill-downs, calculated fields).



Designed S3 Data Lake structure with raw/processed/presentation layers.



Explored AWS Glue ETL pipelines (schema detection, cleaning, aggregation).



Compared Power BI vs QuickSight for visualization and DAX reimplementation.



Phase 2: Data Lake \& ETL Implementation



Created S3 buckets:



raw/ → source sales, inventory, product data.



processed/ → cleaned \& transformed data in Parquet + partitions.



presentation/ → aggregated KPI tables for dashboards.



Built Glue ETL jobs for:



Data cleaning (nulls, duplicates, type consistency).



Transformations (joins, enrichments).



Aggregations (sales summaries, inventory turnover, expiry alerts).



Automated with CloudWatch Events for daily updates.



Phase 3: QuickSight Dashboards



Sales Dashboard: top-selling products, trends, regional heatmaps.



Inventory Dashboard: stock levels, turnover rates, stock-out alerts.



Expiry Alerts: near-expiry products flagged for compliance.



Features: SPICE caching, drill-downs, filters, calculated fields.



Security: IAM integration, RLS for sensitive data, CloudTrail monitoring.



Phase 4: Analysis, Cost, Governance \& Recommendations



Performance: ETL pipelines processed millions of rows efficiently. Partitioned Parquet improved Athena speed and reduced scan cost.



Cost Efficiency:



Pay-per-use Athena queries.



Serverless Glue ETL (billed per run).



QuickSight pay-per-session + SPICE optimization.



Governance: IAM, encryption, audit logs, HIPAA-compliant RLS.



Recommendations:



Keep layered data lake design.



Automate refresh pipelines.



Leverage Lambda for event-driven ETL.



Explore SageMaker for predictive analytics.



Add Kinesis/MSK for real-time streaming analytics.



⚡ Key Benefits



Scalability – Handles millions of records without server upgrades.



Automation – Daily ETL + SPICE refresh eliminates manual work.



Cost Optimization – Pay-as-you-go billing across S3, Athena, Glue, QuickSight.



Governance – Secure, compliant, auditable system.



Future-Ready – Can integrate ML and streaming analytics.



📊 Comparison: On-Prem Power BI vs AWS Cloud Solution

Aspect	Power BI (On-Prem)	AWS Cloud Solution

Infrastructure	Local servers (fixed cost)	Serverless, auto-scale

Data Refresh	Manual / scheduled	Automated via Glue + CloudWatch

Query Performance	Limited by server specs	Partitioned Parquet + Athena

Compliance	Manual governance	IAM, RLS, audit logs

Cost Model	Licensing + infra upkeep	Pay-per-use, cost-efficient

Scalability	Hardware-limited	Virtually unlimited

🚀 Future Roadmap



Lambda triggers → automate ETL on new S3 uploads.



SageMaker integration → predictive demand forecasting, anomaly detection.



Kinesis/MSK → real-time sales \& inventory monitoring.



Embedded QuickSight analytics → dashboards for partners/regulators.



👤 Author



Aman Singh

Data Analyst Intern | AWS Cloud, BI \& Data Strategy Enthusiast

