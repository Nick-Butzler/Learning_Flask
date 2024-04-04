from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world, index"

@app.route('/nick')
def nick():
    n1 = 10 
    n2 = 20 
    sum = n1 + n2
    return str(sum)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
