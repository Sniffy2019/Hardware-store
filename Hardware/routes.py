from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from Hardware import app, db
from Hardware.table import Category, Task


@app.route("/")
def home():
    return render_template("base.html")