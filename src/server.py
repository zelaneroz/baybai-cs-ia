from flask import Flask, request, jsonify
from database_handler import database_handler
app = Flask(__name__)
DATABASE = 'baybai.db'

@app.route('/')
def home():
    return "Hello, Zelan"
