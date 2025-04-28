from flask import Flask, g
import os
from dotenv import load_dotenv
from .routes.item_routes import item_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Carrega as variáveis de ambiente diretamente no app.config
    app.config["WEB3_PROVIDER"] = os.getenv("WEB3_PROVIDER")
    app.config["CONTRACT_ADDRESS"] = os.getenv("CONTRACT_ADDRESS")
    app.config["PRIVATE_KEY"] = os.getenv("PRIVATE_KEY")
    app.config["ABI"] = os.getenv("ABI")

    # Registra blueprints
    app.register_blueprint(item_bp, url_prefix="/api/items")

    return app
