from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/list_prof/<typeOfList>')
def showListProf(typeOfList):
    prof_list = ["Кто","Я", "И", "Почему", "Я", "В списке"]
    return render_template("list_prof.html", typeOfList=typeOfList, prof_list=prof_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
