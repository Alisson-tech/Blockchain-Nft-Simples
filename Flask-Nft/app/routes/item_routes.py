from flask import Blueprint, request, jsonify
from app.services.item_service import create_item, get_all_items

item_bp = Blueprint("item_bp", __name__)

@item_bp.route("/", methods=["POST"])
def add_item():
    data = request.get_json()
    item = create_item(data)
    return jsonify(item), 201

@item_bp.route("/", methods=["GET"])
def list_items():
    items = get_all_items()
    return jsonify(items)