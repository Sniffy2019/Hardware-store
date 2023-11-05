from flask import render_template, request, redirect, url_for
from hardware import app, db
from hardware.table import Product, Item


@app.route("/")
def home():
    items = list(Item.query.order_by(Item.id).all())
    return render_template("shop.html", item=items)


@app.route("/products")
def products():
    products = list(Product.query.order_by(Product.product_name).all())
    return render_template("products.html", products=products)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        product = Product(product_name=request.form.get("product_name"))
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("products"))
    return render_template("add_product.html")


@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.product_name = request.form.get("product_name")
        db.session.commit()
        return redirect(url_for("products"))
    return render_template("edit_product.html", product=product)


@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("products"))


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    products = list(Product.query.order_by(Product.product_name).all())
    if request.method == "POST":
        item = Item(
            item_name=request.form.get("item_name"),
            item_description=request.form.get("item_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            product_id=request.form.get("product_id")
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_item.html", products=products)


@app.route("/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    products = list(Product.query.order_by(Product.product_name).all())
    if request.method == "POST":
        item.item_name = request.form.get("item_name")
        item.item_description = request.form.get("item_description")
        item.is_urgent = bool(True if request.form.get("is_urgent") else False)
        item.due_date = request.form.get("due_date")
        item.product_id = request.form.get("product_id")
        db.session.commit()
    return render_template("edit_item.html", item=item, products=products)


@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))
