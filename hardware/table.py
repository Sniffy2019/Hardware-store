from hardware import db


class Product(db.Model):
    # schema for the Product model
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(25), unique=True, nullable=False)
    items = db.relationship("Item", backref="product",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.product_name


class Item(db.Model):
    # schema for the Item model
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    item_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "product.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Item: {1} | Urgent: {2}".format(
            self.id, self.item_name, self.is_urgent
        )
