from flask import render_template
from Hardware import app, db
from Hardware.table import Category, Task


@app.route("/")
def home():
    return render_template("base.html")