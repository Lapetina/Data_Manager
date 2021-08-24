import os

from pony.orm import Database

db = Database()

if eval(os.getenv("TESTING", "None")):
    db = Database("sqlite", ":memory:")
else:
    db = Database(
        provider="postgres",
        host=os.getenv("DB_HOST"),
        port=8000,
        user="DB_USER",
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("POSTGRE_DATABASE"),
    )
