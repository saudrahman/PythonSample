from flask import Flask

application = Flask(__name__)

@application.route("/")
def welcome():
    return 'Welcome to Sample Python app!'

@application.route("/hello")
@application.route('/hello/<username>')
def hello(username=None):
    if username is not None:
        return "Hello "+username+"!"
    return "Hello world!!!"

if __name__ == "__main__":
    #application.run(host='0.0.0.0', port=80)
    application.run()
