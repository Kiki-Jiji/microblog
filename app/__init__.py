from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object('CONFIG')

from app import routes