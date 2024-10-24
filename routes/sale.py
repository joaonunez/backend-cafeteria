from flask import Blueprint, request, jsonify
from extensions import db

from models.sale import Sale  # Import the Sale model

sale = Blueprint("sale", __name__, url_prefix="/sale")

@sale.route("/", methods=["GET"])
def get_sales():
    sales = Sale.query.all()
    return jsonify([sale.serialize() for sale in sales])
