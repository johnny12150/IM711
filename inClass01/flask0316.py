from flask import Flask
from flask import render_template
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Bootstrap(app)


# 在模板中呼叫巨集的html
@app.route('/marco')
def marco():
    return 'a'


# 將常用部分以html存到templates下作component
@app.route('/component')
def component():
    return 'b'


# falsk內使用繼承
@app.route('/inherit/<index>/<index01>')
def inherit(index, index01):
    # base.html內為基礎網頁內容, 裡面的block可被繼承者修改
    return render_template('index.html', index=index, index01=index01)


@app.route('/bootstrap')
def bootstrap():
    return 'd'


# 錯誤處理
@app.errorhandler(404)
def page404(e):
    # 在裡面設定靜態檔案網址
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)