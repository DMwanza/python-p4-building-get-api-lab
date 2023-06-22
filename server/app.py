#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bakeries=Bakery.query.all()
    response_data=[bakery.to_dict() for bakery in all_bakeries]
    return make_response(jsonify(response_data))

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bake=Bakery.query.filter_by(id=id).first()
    bake_dict=bake.to_dict()

    response=make_response(
        jsonify(game_dict),
        200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    sorted_baked=BakedGood.query.order_by(BakedGood.price.desc()).all()
    response_data = [baked_good.to_dict() for baked_good in sorted_baked]
    return make_response(jsonify(response_data))

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if most_expensive:
        response_data = most_expensive.to_dict()
        return make_response(jsonify(response_data))
    return make_response(jsonify({'message': 'No baked goods found'}), 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
