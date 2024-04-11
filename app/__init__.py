from flask import Flask
from app.controllers.weather_controller import weather_controller

def create_app():
    app = Flask(__name__)
    app.register_blueprint(weather_controller)

    return app