from flask import Flask

app = Flask(__name__)

@app.route('/')
def hime():
    return "It's alive!"

app.run(port=5000, debug=True)
