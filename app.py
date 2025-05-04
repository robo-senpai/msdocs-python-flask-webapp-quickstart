from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/workout', methods=['GET', 'POST'])
def workout():
    return render_template('workout.html')

def countdown_timer(duration_in_seconds):
    """Simulate a countdown using Python (for accuracy)"""
    remaining_time = duration_in_seconds
    while remaining_time > 0:
        time.sleep(1)  # Sleep for 1 second (accurately)
        remaining_time -= 1
        socketio.emit('timer_update', {'time_left': remaining_time}) # Send the updated time to client

@socketio.on('start_timer')
def start_timer(data):
    """Start the countdown timer when the client clicks start"""
    # exercise_name = data.get('exercise_name')
    duration_in_minutes = int(data.get('duration'))
    duration_in_seconds = duration_in_minutes * 60
    countdown_timer(duration_in_seconds)

if __name__ == '__main__':
    socketio.run(app, debug=True)