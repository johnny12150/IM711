from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>', 401


@app.route('/user/<name>')
def show_name(name):
    return f'<h1>good {name}</p>'


# 抓request header的內容
@app.route('/info/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return f'{user_agent}'


# 使用basic的html template
@app.route('/about')
def about():
    # render_template會自動去templates資料夾下取html
    return render_template('about.html')


# 傳參數到html的template
@app.route('/tmp/<word>')
def passVar(word):
    # 可以接收很多種類型的variables,像是dictionary, list等
    return render_template('tmp.html', word=word)


# 讀取path(/)
@app.route('/path/<path:somepath>')
def showPath(somepath):
    return '{}'.format(somepath)


if __name__ == '__main__':
    app.run(debug=True)