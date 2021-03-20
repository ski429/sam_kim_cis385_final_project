from flask import render_template, redirect, request, jsonify
from app import app
from app.models import Item


@app.route('/')
def home():
    query = Item.query.all()
    return render_template('index.html', menu=query)
