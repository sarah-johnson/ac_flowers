from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html", thing_to_say = 'hello')


if __name__ == '__main__':
    app.run()
