from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1 style='background-color:red'>Hello World</h1>"

@app.route('/new')
def new():
    return "<h1 style='background-color:cyan'>new page</h1>"


@app.route('/profile/<name>')
def profile(name):
    return f'<p>This profile belongs to <strong>{name}</strong></p>'

@app.route("/admin")
def hello_admin():
    return "<h1>Hello admin</h1>"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"<h1>Hello guest {guest}</h1>"

@app.route("/user/<name>")
def hello_user(name):
    if name=="admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))

@app.route("/success/<name>")
def success(name):
    return f"<h1>Welcome {name}</h1>"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['nm']
        return redirect(url_for('success', name = username))
    else:
        username = request.args.get("nm")
        return redirect(url_for('success', name = username))

@app.route("/welcome/<name>")
def index(name):
    return render_template('hello.html', name=name)

@app.route("/student")
def student():
    return render_template('student.html')

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template('result.html', result = result)


if __name__ == '__main__':
    app.run()