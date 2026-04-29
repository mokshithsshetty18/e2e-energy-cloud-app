from flask import Flask, render_template, request, jsonify
import sqlite3
import encryption_utils
import os

app = Flask(__name__)

# Database helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/generate-key', methods=['GET'])
def generate_key_route():
    key = encryption_utils.generate_key()
    return jsonify({"key": key})

@app.route('/api/encrypt', methods=['POST'])
def encrypt_route():
    data = request.json
    sender = data.get('sender', 'Anonymous')
    message = data.get('message')
    key = data.get('key')
    
    if not message or not key:
        return jsonify({"error": "Message and Key are required"}), 400
    
    try:
        encrypted = encryption_utils.encrypt_message(message, key)
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (title, encrypted_payload) VALUES (?, ?)',
                     (sender, encrypted))
        conn.commit()
        conn.close()
        return jsonify({"success": True, "encrypted": encrypted})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(m) for m in messages])

@app.route('/api/decrypt', methods=['POST'])
def decrypt_route():
    data = request.json
    payload = data.get('payload')
    key = data.get('key')
    
    if not payload or not key:
        return jsonify({"error": "Payload and Key are required"}), 400
    
    decrypted = encryption_utils.decrypt_message(payload, key)
    return jsonify({"decrypted": decrypted})

if __name__ == '__main__':
    # Initialize DB if not exists or if table needs update
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            encrypted_payload TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    app.run(debug=True, port=5000)

