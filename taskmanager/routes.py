from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_categories", methods=["GET","POST"])
def category():
    return render_template("add_category.html")
