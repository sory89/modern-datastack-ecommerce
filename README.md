# 🛒 Modern Data Stack Ecommerce Pipeline

End-to-end **Modern Data Engineering pipeline** that captures ecommerce data changes, streams them through Kafka, transforms them with DBT, and orchestrates workflows with Airflow.

---

## 🚀 Tech Stack

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000000?style=for-the-badge&logo=apache-kafka&logoColor=white)
![Debezium](https://img.shields.io/badge/Debezium-EA1C24?style=for-the-badge&logo=debezium&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-222222?style=for-the-badge&logo=githubactions&logoColor=white)

---

## 🏗️ Architecture

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1e42ab85-f112-4258-9f0c-6272b36f6376" />

⚙️ Pipeline Overview

This project demonstrates a Modern Data Stack pipeline that processes ecommerce transactional data in real-time using streaming and ELT architecture.

Pipeline Flow:

Data Generator → Simulates banking transactions, accounts & customers (via Faker).
Kafka + Debezium → Streams change data (CDC) into MinIO (S3-compatible storage).
Airflow → Orchestrates data ingestion & snapshots into Snowflake.
PostgreSQL → Data Warehouse (Bronze → Silver → Gold).
DBT → Applies transformations, builds marts & snapshots (SCD Type-2).
CI/CD with GitHub Actions → Automated tests, build & deployment.

Key features

Change Data Capture using Debezium

Real-time streaming with Apache Kafka

Data lake storage using MinIO (S3 compatible)

Data transformation using dbt

Workflow orchestration using Apache Airflow

Business analytics using Power BI

🏗 Medallion Architecture

The project follows the Bronze / Silver / Gold architecture.

🥉 Bronze (Raw)

Raw ingestion from Kafka events.

Characteristics:

immutable data

JSON ingestion

historical replay possible

🥈 Silver (Cleaned)

Cleaned and structured datasets.

Transformations include:

schema normalization

data validation

deduplication

🥇 Gold (Business)

Business-ready datasets.

<img width="937" height="467" alt="image" src="https://github.com/user-attachments/assets/9b947cfa-ca99-4ff9-bca1-6291cf1a7ec1" />


<img width="538" height="337" alt="image" src="https://github.com/user-attachments/assets/77c27726-9836-46b0-8a7d-837b280f5058" />



