from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/home")
def homePage():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)