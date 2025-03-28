from flask import Blueprint, jsonify
import datetime

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/test', methods=['GET'])
def test_endpoint():
    """Приклад ендпоінту, що повертає JSON"""
    return jsonify({
        "status": "success",
        "message": "Hello from Flask Backend!",
        "timestamp": datetime.datetime.now().isoformat(),
        "data": {
            "user": "Anonymous",
            "items": [1, 2, 3]
        }
    })

@api_blueprint.route('/echo', methods=['POST'])
def echo_endpoint():
    """Ендпоінт, що повертає отримані дані"""
    from flask import request
    return jsonify({
        "status": "success",
        "received_data": request.json
    })