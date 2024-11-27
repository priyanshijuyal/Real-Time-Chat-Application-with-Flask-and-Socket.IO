from flask import Flask, render_template
from flask_socketio import SocketIO
import os

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", os.urandom(24))

# Set up Redis URL with TLS
redis_password = os.getenv('UPSTASH_REDIS_PASSWORD')
redis_host = os.getenv('UPSTASH_REDIS_HOST')
redis_port = int(os.getenv('UPSTASH_REDIS_PORT', 6379))
redis_url = f"rediss://:{redis_password}@{redis_host}:{redis_port}"

# Initialize SocketIO with Redis message queue
socketio = SocketIO(app, message_queue=redis_url, cors_allowed_origins="*")

# WebSocket handlers
@socketio.on("connect")
def handle_connect():
    print("Client connected.")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected.")

@socketio.on("message")
def handle_message(data):
    """Handle incoming chat messages."""
    print(f"Message received: {data}")
    # Broadcast the message to all connected clients except the sender
    socketio.emit("message", data, include_self=False)

# Serve the chat HTML page
@app.route("/")
def index():
    return render_template("chat.html")  # Render the chat interface template

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=8000)
