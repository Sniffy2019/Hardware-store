from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from hardware import app, db
from hardware.table import Category, Task


@app.route("/")
def home():
    return render_template("shop.html")