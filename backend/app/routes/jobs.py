from flask import Blueprint, jsonify, request

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/", methods=["GET"])
def search_jobs():
    keyword = request.args.get("q", "")
    return jsonify({"message": f"Szukam ofert dla: {keyword}", "jobs": []})
