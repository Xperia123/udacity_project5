from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is The Capstone Project DevOps Udacity, \
            my name is Nguyen Huu Dai</h1>'

app.run(host='0.0.0.0', port=80)
