from flask import Flask, abort, request, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema, product_schema

@app.route('/')
def home():
    products = db.session.query(Product).all()
    return render_template('home.html', products=products)

@app.route('/<int:id>')
def product_html(id):
    product = db.session.query(Product).get(id)
    return render_template('product.html', product=product)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    product = db.session.query(Product).get(product_id) # SQLAlchemy request => 'SELECT * FROM products'
    return product_schema.jsonify(product)

@app.route('/products', methods=['POST'])
def post_products():
    product_name = request.get_json()["name"]
    new_product = Product()
    new_product.name = product_name
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = db.session.query(Product).get(product_id)
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return "", 204
    abort(404)

@app.route('/products/<int:product_id>', methods=['PATCH'])
def patch_product(product_id):
    product = db.session.query(Product).get(product_id)
    if product_id is not None:
        new_product_name = request.get_json()["name"]
        if new_product_name == "":
            abort(422)
        product.name = new_product_name
        db.session.commit()
        return "", 204
    abort(404)
