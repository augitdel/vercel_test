import time
import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def random_number():
    return render_template('random_number.html')

def generate_random_number():
    while True:
        time.sleep(5)
        number = random.randint(1, 100)
        socketio.emit('update_number', {'number': number})

if __name__ == '__main__':
    socketio.start_background_task(generate_random_number)
    socketio.run(app, debug=True)