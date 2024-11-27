# Real-Time Chat Application with Flask and Socket.IO

This project is a simple real-time chat application built using Flask and Flask-SocketIO. It allows users to send and receive messages in real-time using WebSockets and Redis for message queueing.

## Features

- **Real-time messaging:** Send and receive messages instantly.
- **User-friendly UI:** The chat interface is designed to be clean and responsive.
- **Redis-backed:** Uses Redis (via Upstash) to manage message queues in a distributed system.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.7+
- `pip install flask flask-socketio redis`

## Installation

1. **Clone the repository or download the project files.**

2. **Install required dependencies:**
   Run the following command to install all necessary Python libraries:

   ```bash
   pip install -r requirements.txt
