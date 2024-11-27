# Real-Time Chat Application with Flask and Socket.IO

## Overview

Welcome to the Real-Time Chat Application repository! This project demonstrates a simple real-time messaging system built using Flask and Flask-SocketIO. The application allows users to send and receive messages instantly via WebSockets, with Redis (hosted on Upstash) used to handle message queues in a distributed system.

## Features

- **Real-time messaging:** Users can send and receive messages in real-time.
- **User-friendly UI:** The chat interface is clean, modern, and responsive.
- **Redis-backed:** Utilizes Redis via Upstash for managing message queues, ensuring scalability and reliability.
- **WebSocket Integration:** Flask-SocketIO powers the WebSocket communication, making it ideal for real-time applications.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.7+
- Redis (Upstash or local)
- Necessary Python packages:
  - `flask`
  - `flask-socketio`
  - `redis`

To install these dependencies, you can use the `requirements.txt` file.

## Installation

### 1. Clone the repository or download the project files:
```bash
git clone https://github.com/priyanshijuyal/real-time-chat.git
cd real-time-chat
