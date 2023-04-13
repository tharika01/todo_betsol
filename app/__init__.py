"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrptlvdvk4rjsv88gq0-a.oregon-postgres.render.com",
        database="todo_5zhw",
        user="todo_5zhw_user",
        password="lsGYyWybQuusxsDCn6mBLkAg2h5rrRK1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
