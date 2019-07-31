import markdown
import os
import shelve

#imp0rt the flask framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("orders.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


class OrderList(Resource):
  def get(self):
    shelf = get_db()
    keys = list(shelf.keys())
    orders = []

    for key in keys:
      orders.append(shelf[key])

    return { 'message': 'Success', 'data': orders }, 200

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=True)
    parser.add_argument('quantity', required=True)
    parser.add_argument('productName', required=True)

    args = parser.parse_args()
    shelf = get_db()
    if (args['id'] in shelf):
      return { 'message': 'Order already exists', 'data': {} }, 409

    shelf[args['id']] = args

    return { 'message': 'Order created', 'data': args }, 201

class Order(Resource):
  def get(self, id):
    shelf = get_db()

    #if key doesn't exist, return 404
    if not (id in shelf):
      return { 'message': 'Order not found', 'data': {} }, 404

    return { 'message': 'Order found', 'data': shelf[id] }, 404

  def delete(self, id):
    shelf = get_db()

    #if key doesn't exist, return 404
    if not (id in shelf):
      return { 'message': 'Order not found', 'data': {} }, 404

    del shelf[id]
    return '', 204


api.add_resource(OrderList, '/api/orders')
api.add_resource(Order, '/api/orders/<string:id>')