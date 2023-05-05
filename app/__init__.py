"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa7oqk728r8862hl60-a.oregon-postgres.render.com",
        database="todo_1cts",
        user="root",
        password="0IaSleSgrM2M1jumKQeV8tGSrnuFM5R0")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
