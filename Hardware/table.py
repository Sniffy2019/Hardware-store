from Hardware import db


class Selection(db.table):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    Selection = db.relationship("selection", backref="Hardware", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.table):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    Hardware_name = db.Column(db.String(50), unique=True, nullable=False)
    Hardware_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    Hardware_id = db.Column(db.Integer, db.ForeignKey("Hardware.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )