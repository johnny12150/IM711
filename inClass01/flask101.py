from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>', 401

@app.route('/user/<name>')
def showName(name):
    return f'<h1>good {name}</p>'

@app.route('/info/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return f'{user_agent}'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)