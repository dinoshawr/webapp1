from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')

@application.route('/davidscock')
def david():
    return "Is fat"

@application.route('/jah')
def davidd():
    return "Get jahb8ed khed"


if __name__ == "__main__":
    application.run(debug=True, port=5000) #turn debug off for prodcution deployment
