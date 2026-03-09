import pandas as pd
import numpy as np
import random
import psycopg2
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

# CONFIGURATION
NUM_RECORDS = 1000
ERROR_PERCENTAGE = 0.08

countries = ["US", "UK", "IN", "DE", "FR", "CA", "AU"]
categories = ["Electronics", "Clothing", "Home", "Books", "Sports"]
payment_methods = ["Credit Card", "PayPal", "UPI", "Debit Card"]

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", 5432),
    "dbname": os.getenv("POSTGRES_DB", "marketingdb_source"),
    "user": os.getenv("POSTGRES_USER", "marketinguser"),
    "password": os.getenv("POSTGRES_PASSWORD", "marketingpass"),
}

def generate_data():
    data = []

    for i in range(NUM_RECORDS):
        order_date = fake.date_between(start_date='-1y', end_date='today')
        quantity = random.randint(1, 5)
        price = round(random.uniform(10, 500), 2)

        data.append({
            "transaction_id": f"T{i+1}",
            "order_date": order_date,
            "customer_id": f"C{random.randint(1, 300)}",
            "customer_name": fake.name(),
            "country": random.choice(countries),
            "product_id": f"P{random.randint(1, 200)}",
            "product_category": random.choice(categories),
            "quantity": quantity,
            "price": price,
            "payment_method": random.choice(payment_methods),
            "order_status": random.choice(["Completed", "Cancelled", "Returned"])
        })

    df = pd.DataFrame(data)
    inject_errors(df)
    insert_to_postgres(df)

def inject_errors(df):
    num_errors = int(len(df) * ERROR_PERCENTAGE)

    for _ in range(num_errors):
        row = random.randint(0, len(df) - 1)
        error_type = random.choice([
            "null_customer",
            "negative_quantity",
            "invalid_price",
            "future_date",
            "invalid_country",
            "duplicate_transaction"
        ])

        if error_type == "null_customer":
            df.at[row, "customer_id"] = None
        elif error_type == "negative_quantity":
            df.at[row, "quantity"] = -random.randint(1, 5)
        elif error_type == "invalid_price":
            df.at[row, "price"] = -random.uniform(1, 100)
        elif error_type == "future_date":
            df.at[row, "order_date"] = datetime.now() + timedelta(days=30)
        elif error_type == "invalid_country":
            df.at[row, "country"] = "XYZ"
        elif error_type == "duplicate_transaction":
            df.at[row, "transaction_id"] = "T1"

def insert_to_postgres(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Créer la table si elle n'existe pas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ecommerce_sales (
            transaction_id   VARCHAR(50),
            order_date       DATE,
            customer_id      VARCHAR(50),
            customer_name    VARCHAR(255),
            country          VARCHAR(10),
            product_id       VARCHAR(50),
            product_category VARCHAR(100),
            quantity         INTEGER,
            price            NUMERIC(10, 2),
            payment_method   VARCHAR(50),
            order_status     VARCHAR(50)
        );
    """)

    # Insérer les données
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO ecommerce_sales (
                transaction_id, order_date, customer_id, customer_name,
                country, product_id, product_category, quantity,
                price, payment_method, order_status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row["transaction_id"],
            row["order_date"],
            row["customer_id"],
            row["customer_name"],
            row["country"],
            row["product_id"],
            row["product_category"],
            row["quantity"] if pd.notna(row["quantity"]) else None,
            row["price"] if pd.notna(row["price"]) else None,
            row["payment_method"],
            row["order_status"]
        ))

    conn.commit()
    cur.close()
    conn.close()
    print(f"{len(df)} records inserted into PostgreSQL.")

if __name__ == "__main__":
    generate_data()