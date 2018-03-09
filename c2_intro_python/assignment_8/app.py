from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Joel's first web application"

@app.route('/helloworld')
def helloworld():
    return "<h1>Hello, world<h1>"

@app.route('/currentservertime')
def currentservertime():
    time = str(datetime.now())
    return time

if __name__ == '__main__':
    app.run(port=5000, debug=True)

