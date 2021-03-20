from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


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
    order_total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Item('{self.order_total}', '{self.id}')"


class ItemsByOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))


menu = [
    {
        'name': 'sausage pizza',
        'pic': 1,
        'cost': 10
    },
    {
        'name': 'pepperoni pizza',
        'pic': 2,
        'cost': 10
    },
    {
        'name': 'cheese pizza',
        'pic': 3,
        'cost': 7
    }
]


@app.route('/')
def home():
    return render_template('index.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
