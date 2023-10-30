from flask import Flask, request, jsonify
from database_handler import database_handler


app = Flask(__name__)
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
DATABASE = 'sample.db'

@app.route('/')
def home():
    return "Hello, Zelan"

@app.route('/send_text', methods=['POST','GET'])
def send_text():
    data = request.get_json()
    return jsonify(data)

@app.route('/get_string')
def get_string():
    x = 'sample2'
    # return jsonify({'string': x})
    return jsonify(x)

if __name__ == '__main__':
    app.run(port=5000)
