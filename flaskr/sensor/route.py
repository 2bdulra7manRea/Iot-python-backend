from flask import Blueprint
from .sensor import Sensor
from ..clients.client import jwt_guard
from flask import request

sensor_route = Blueprint('sensor', __name__, url_prefix='/sensor')


@sensor_route.post('/register/')
@jwt_guard
def register():
    sensor = Sensor()
    return sensor.register(request.get_json()['sensor_id'])


@sensor_route.post('/submit')
@jwt_guard
def submit():
    sensor = Sensor()
    data = request.get_json()
    return sensor.submit_data(data=data)


@sensor_route.route('/<int:id>')
@jwt_guard
def fetch_by_id(id: int):
    sensor = Sensor()
    return sensor.fetch_data_by_sensor_id(sensor_id=id)


@sensor_route.route('/all')
@jwt_guard
def fetch_all():
    sensor = Sensor()
    return sensor.get_all_sensors_data()
