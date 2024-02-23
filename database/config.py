import os

database=os.environ.get("POSTGRES_DB")
host=os.environ.get("POSTGRES_HOST")
user=os.environ.get("POSTGRES_USER")
password=os.environ.get("POSTGRES_PASSWORD")
port="5432"