from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! This is a test to commit to Michael's dev remote branch"


if __name__ == '__main__':
    app.run()
