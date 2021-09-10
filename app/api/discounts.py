"""Endpoints used for data entry"""
import traceback

from flask import Blueprint
from flask import jsonify
from flask import request
from app.discounts import calculate_discounts

discounts = Blueprint("discounts", __name__)


@discounts.route("/<string:user_type>", methods=["POST"])
def calculate_net_payable_amount(user_type="customer"):
    """Given a bill, return the net payable amount"""
    _data = request.get_json()
    try:
        return jsonify(
            amount=calculate_discounts(
                user_type=user_type,
                amount=_data.get("amount"),
                years=_data.get("years"),
                grocery_p=True
                if _data.get("grocery_p").lower() == "true" else False))
    # pylint: disable=W0703
    except Exception:
        print(traceback.format_exc())
        return jsonify(
            status=128,
            message="Check your request data")
