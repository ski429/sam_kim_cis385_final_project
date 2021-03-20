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
        db.session.commit()
        return redirect(f'/order_details/{new_order_id}')

    else:
        return render_template('index.html', menu=menu_query)


@app.route('/order_details/<int:order_num>', methods=['GET'])
def order_detail(order_num):
    # Accumulator for cost of order (initialized with default of 0)
    total = 0
    # Multiple table join to get complete order information
    order_placed = db.session.query(Order, ItemsByOrder, Item)\
          .join(ItemsByOrder, ItemsByOrder.order_id == Order.id)\
          .join(Item, Item.id == ItemsByOrder.item_id).filter(Order.id==order_num)
    # Retrieve ItemsByOrder.qty and Item.item_cost to calc total cost
    for item in order_placed:
        if item[1].qty and item[1].qty > 0:
            total += item[1].qty * item[2].item_cost
    # Update missing Order.order_total
    db.session.commit()
    return render_template('your_order_details.html', data=order_placed)


@app.route('/order_cancel/<int:order_num>', methods=['DELETE'])
def delete_order(order_num):
    order_to_delete = Order.query.filter_by(order_id=order_num)
    db.session.delete(order_to_delete)
    db.session.commit()
    return render_template('order_canceled.html', order_id=order_num)

