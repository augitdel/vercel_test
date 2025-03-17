import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('5sec.html')

@app.route('/generate_number', methods=['POST'])
def generate_number():
    number = random.randint(1, 100)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True)