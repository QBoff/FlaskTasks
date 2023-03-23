from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def base():
    return render_template("base.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/training/<prof>')
def show_prof(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("math_prof.html")
    
    return render_template("science_prof.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
