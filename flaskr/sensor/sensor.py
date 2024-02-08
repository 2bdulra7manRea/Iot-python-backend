from ..sensor.model import create, fetch
from ..sensor.register_model import register_new_sensor, fetch_by_sensor_id

class Sensor:

    def register(self, id):
        register_new_sensor(id)
        return {"message": "sensor has been registered successfully"}

    def submit_data(self, data):
        sensor_registered = self.fetch_data_by_sensor_id(
            sensor_id=data["sensor_id"])
        if (not sensor_registered or not sensor_registered['sensor_id']):
            return {"message": "the sensor is not registered yet!"},400

        create(sensor_id=data['sensor_id'],
               temperature=data['temperature'], timestamps=data['timestamps'])
        return {"message": "submitted successfully"}

    def get_all_sensors_data(self):
        return fetch()

    def fetch_data_by_sensor_id(self, sensor_id):
        return fetch_by_sensor_id(sensor_id=sensor_id)
