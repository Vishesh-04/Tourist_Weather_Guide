# backend.py
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    send(jsonify({'sender': 'bot', 'text': 'Hello from the backend!'}))

@app.route('/send_message/', methods=['POST'])
def send_message():
    message = request.json.get('text')
    if message:
        send(jsonify({'sender': 'user', 'text': message}))
    return jsonify({'success': True})

if __name__ == '__main__':
    socketio.run(app, debug=True)
