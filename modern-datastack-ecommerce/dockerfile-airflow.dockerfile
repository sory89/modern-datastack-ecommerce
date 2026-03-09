FROM apache/airflow:3.1.7

USER root
COPY create_admin.sh /opt/airflow/create_admin.sh
RUN chmod +x /opt/airflow/create_admin.sh

USER airflow

RUN pip install --no-cache-dir \
    boto3 \
    fastparquet \
    sqlalchemy \
    psycopg2-binary \
    pandas