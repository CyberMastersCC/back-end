from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return jsonify({"message": "Hello, Flask in Docker!"})

def init_routes(app):
    app.register_blueprint(main)
