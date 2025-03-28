from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Налаштування CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://frontend:3000"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Реєстрація блюпрінтів
    from .routes import api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app