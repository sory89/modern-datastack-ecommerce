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

Data Source (PostgreSQL Ecommerce DB)
        │
        │ CDC
        ▼
Debezium + Kafka
        │
        ▼
Object Storage (MinIO / S3)
        │
        ▼
Raw Layer (Bronze)
        │
        ▼
dbt Transformations
        │
        ▼
Cleaned Layer (Silver)
        │
        ▼
Business Layer (Gold)
        │
        ▼
Power BI / Analytics

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/1e42ab85-f112-4258-9f0c-6272b36f6376" />


