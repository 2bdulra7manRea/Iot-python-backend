import os
from flask import Flask
from .clients.route import client_route
from .sensor.route import sensor_route
from .db.database import init_db


def create_app(test_config=None):
    try:
        init_db()
        app = Flask(__name__, instance_relative_config=True)
        app.register_blueprint(client_route)
        app.register_blueprint(sensor_route)

        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        @app.route('/hello')
        def hello():
            return 'Hello, World!'

        return app
    except Exception as e:
        print("unable to start the server!")
        print(e)
