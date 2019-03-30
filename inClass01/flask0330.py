from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my hard to guess string'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None

    form = NameForm()

    if form.validate_on_submit():
        # 舊的輸入值
        name = form.name.data
        # 清除預設值
        form.name.data = ""

    return render_template('form.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
