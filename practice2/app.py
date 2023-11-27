from flask import Flask, request, jsonify
import sqlite3
from database_handler import database_handler

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('remote_notes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/upload_note', methods=['POST','GET'])
def upload_note():
    # note_content = request.get_json()['content']
    note_content = request.get_json()['content']
    x = database_handler(namedb='remote_notes.db')
    x.run_query("CREATE TABLE if not exists notes(content TEXT);")
    x.run_query('INSERT INTO notes (content) VALUES (?);',(note_content,))
    x.close()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
