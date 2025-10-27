from flask import Blueprint, jsonify, request

cv_bp = Blueprint("cv", __name__)

@cv_bp.route("/", methods=["POST"])
def create_cv():
    data = request.json
    return jsonify({"message": "CV zapisane", "data": data})
