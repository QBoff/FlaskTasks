from flask import Flask, redirect, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/distribution')
def distribution():
    list_of_astronautes = [("Ридди Скот", "капитан корабля"),
                           ("Энди Уори", ""),
                           ("Марк Уотни", ""),
                           ("Венката Капур", ""),
                           ("Тедди Сандерс", "")]
    
    return render_template("distribution.html",
                           list_of_astronautes=enumerate(list_of_astronautes), title="По каютам!")


@app.route('/table/<string:sex>/<int:age>')
def show_table(sex, age):
    return render_template("table.html", sex=sex, age=age)




if __name__ == '__main__':
    app.run()