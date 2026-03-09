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

Business-ready datasets:

Examples:

daily revenue

top selling products

customer lifetime value

order trends

🚀 DevOps & DataOps

This project integrates DevOps best practices for data platforms.

Containerized Infrastructure

All services run with Docker.

Docker Services
 ├── PostgreSQL
 ├── Kafka
 ├── Debezium
 ├── MinIO
 ├── Airflow
 └── dbt
CI/CD Pipeline

Using GitHub Actions:

Pipeline includes:

1. Code validation
2. Python linting
3. dbt tests
4. Docker build
5. Pipeline deployment
📦 Project Structure
modern-datastack-ecommerce
│
├── docker-compose.yml
├── consumer
│
├── kafka-debezium
│
├── marketing_dbt
│
├── data-source
│
├── docker
│
└── dags
💻 Skills Demonstrated

This project demonstrates skills in:

Data Engineering

Real-time data pipelines

Change Data Capture

Streaming architectures

Data Lakehouse design

ELT workflows

DataOps / DevOps

Technologies used:

Kafka
Debezium
Airflow
dbt
PostgreSQL
MinIO
Docker
GitHub Actions
🧠 Why This Project Matters

This architecture represents modern production-grade data platforms used in industry, including:

ecommerce analytics

real-time monitoring

event-driven architectures

scalable data pipelines

📈 Future Improvements

Possible extensions:

Data quality monitoring

Great Expectations

OpenLineage

Data Catalog (DataHub)

Kubernetes deployment

👨‍💻 Author

Sory Diallo

Data Engineer | DataOps | DevOps

