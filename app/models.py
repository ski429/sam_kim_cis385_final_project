from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(20), unique=True)
    item_cost = db.Column(db.Float)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.item_name}', '{self.id}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_time = db.Column(db.DateTime, nullable=False)
    order_items = db.relationship('ItemsByOrder', backref='items')
    order_total = db.Column(db.Float, nullable=False, default=0)

    def __repr__(self):
        return f"Item('{self.order_total}', '{self.id}')"


class ItemsByOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def __repr__(self):
        return f"ItemsByOrder('qty: {self.qty}', 'item: {self.item_id}', 'order number: {self.order_id}')"
