from flask import Flask

application = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world!!"


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
