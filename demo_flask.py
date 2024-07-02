from  flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Hello, How are you?"

@app.route('/name')
def show_name():
    return "Bipul Kumar Shahi"

app.run()