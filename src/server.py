from flask import Flask, request, jsonify
import sqlite3
from database_handler import database_handler
import jwt

app = Flask(__name__)
DATABASE = 'remote.db'


@app.route('/protected', methods=['POST'])
def protected_route():
    data = request.get_json()
    token = data.get('token') if data else None

    if not token:
        return jsonify({'message': 'No token provided'}), 401

    try:
        payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        x = database_handler(namedb=DATABASE)
        posts = x.search2("""SELECT username,title,content,timestamp FROM posts3""")
        return jsonify({'success': True, 'data': posts}), 200
        # return jsonify({'success': True, 'data': payload}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401


# @app.route('/protected', methods=['POST'])
# def protected_route():
#     data = request.get_json()
#     token = data.get('token') if data else None
#
#     if not token:
#         return jsonify({'message': 'No token provided'}), 401
#
#     try:
#         payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
#         # Perform your logic here
#         # e.g., you might want to return some user-specific data based on the token
#
#         # Return success response (could include the decoded payload or other data)
#         return jsonify({'success': True, 'data': payload}), 200
#
#     except jwt.ExpiredSignatureError:
#         return jsonify({'message': 'Token expired'}), 401
#     except jwt.InvalidTokenError:
#         return jsonify({'message': 'Invalid token'}), 401


@app.route('/upload_post', methods=['POST','GET'])
def upload_post():
    # note_content = request.get_json()['content']
    # data = request.json
    a = request.get_json()
    title,content,timestamp,uname = a['title'],a['content'],a['timestamp'],a['username']
    if not all([title, content, timestamp, uname]):
        return jsonify({'error': 'Missing data'}), 400

    x = database_handler(namedb=DATABASE)
    # x.run_query("CREATE TABLE if not exists posts3(title TEXT);")
    x.run_query('INSERT INTO posts3 (title,content,timestamp,username) VALUES (?,?,?,?);',(title,content,timestamp,uname))
    x.close()
    # return jsonify(title)
    return jsonify({'message': 'Post uploaded successfully'}), 200


if __name__ == '__main__':
    app.run(port=5000)

