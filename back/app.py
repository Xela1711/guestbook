import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# config depuis docker-compose
app.config['MYSQL_HOST']     = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_USER']     = os.getenv('DB_USER', 'guestuser')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', 'guestuserpwd')
app.config['MYSQL_DB']       = os.getenv('DB_NAME', 'guestdb')

mysql = MySQL(app)

@app.route('/api/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute(
      "INSERT INTO messages (name, message) VALUES (%s,%s)",
      (data['name'], data['message'])
    )
    mysql.connection.commit()
    cur.close()
    return jsonify(status='ok'), 201

@app.route('/api/messages', methods=['GET'])
def get_messages():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, message, created_at FROM messages ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    return jsonify([
      {'id': r[0], 'name': r[1], 'message': r[2], 'created_at': r[3].isoformat()}
      for r in rows
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
