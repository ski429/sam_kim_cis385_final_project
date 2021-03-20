from flask import render_template, redirect, request, url_for
from app import app, db
from app.models import Item, ItemsByOrder, Order
import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    menu_query = Item.query.all()

    if request.method == 'POST':
        new_order = Order(order_time=datetime.datetime.now())
        db.session.add(new_order)
        db.session.commit()
        new_order_id = new_order.id
        for item in menu_query:
            quantity = request.form[f'item{item.id}']
            new_item_by_order = ItemsByOrder(qty=quantity, item_id=item.id, order_id=new_order_id)
            db.session.add(new_item_by_order)
            print(new_item_by_order)
        db.session.commit()
        return redirect('/order_details')

    else:
        return render_template('index.html', menu=menu_query)


@app.route('/order_details', methods=['GET'])
def order_detail():
    return render_template('your_order_details.html')
