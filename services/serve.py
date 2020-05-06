from flask import Flask
from services.config import Development

app = Flask(__name__)
app.config.from_object(Development)
