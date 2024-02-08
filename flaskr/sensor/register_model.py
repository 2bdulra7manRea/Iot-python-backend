from sqlalchemy import Column, Integer, String, select
from ..db.database import Base, db_session


class SensorRegister(Base):
    __tablename__ = 'sensors_registered'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, unique=True)

    def __init__(self, sensor_id=None):
        self.sensor_id = sensor_id

    def __repr__(self):
        return f'<Sensor {self.sensor_id!r}>'


def register_new_sensor(sensor_id):
    u = SensorRegister(sensor_id=sensor_id)
    db_session.add(u)
    db_session.commit()


def fetch_all_registered_sensor():
    list = []
    stmt = select(SensorRegister).where()
    for sensor in db_session.scalars(stmt):
        list.append({
            "sensor_id": sensor.sensor_id,
        })
    return list


def fetch_by_sensor_id(sensor_id):
    list = []
    stmt = select(SensorRegister).where(SensorRegister.sensor_id == sensor_id)
    print(stmt)
    for sensor in db_session.scalars(stmt):
        list.append({
            "sensor_id": sensor.sensor_id,
        })

    if (list and list[0]):
        return list[0]

    return []
