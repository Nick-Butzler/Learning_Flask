from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nick")
def nick():
    n1 = 10 
    n2 = 20 
    sum = n1 + n2
    return str(sum)

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(port=5000, debug=True)
=======
if __name__ == '__main__':
    app.run(debug=True, port=8000)
>>>>>>> 3780a27c48fca24bcfe9fb30f534132db54c1c00
