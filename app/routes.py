from flask import render_template, url_for
from app import app
from app.models import Item, Order, ItemsByOrder


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