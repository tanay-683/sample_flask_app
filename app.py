from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello buddy, im deployed'

@app.route('/index')
def index():
    return render_template('index.html')

