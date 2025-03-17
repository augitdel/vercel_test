from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('socket_index.html')

@app.route('/trigger_update')
def trigger_update():
    # Your function logic here
    data = {"message": "Updated content from Flask!"}
    socketio.emit('update_content', data)
    return "Update triggered"

if __name__ == '__main__':
    socketio.run(app, debug=True)