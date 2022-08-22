import logging

from flask import Flask
from card_app.database.db_session import create_tables

from card_app.services.insert_bd import insert_tag


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.NOTSET
)

app = Flask(__name__)
db = create_tables()

populate_db = insert_tag('all')


from .all_routes import *
