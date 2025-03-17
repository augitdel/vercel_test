import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('socket_index.html')

@app.route('/generate_number', methods=['POST'])
def generate_number():
    number = random.randint(1, 100)
    return jsonify({'number': number})

@app.route('/generate_number2', methods=['POST'])
def generate_number2():
    number2 = random.randint(100, 200)
    return jsonify({'number': number2})

if __name__ == '__main__':
    app.run(debug=True)