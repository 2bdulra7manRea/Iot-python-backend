from sqlalchemy import Column, Integer, String, select
from ..db.database import Base, db_session


class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, unique=False)
    temperature = Column(Integer, unique=False)
    timestamps = Column(String(120), unique=False)

    def __init__(self, sensor_id=None, temperature=None, timestamps=None):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.timestamps = timestamps

    def __repr__(self):
        return f'<Sensor {self.sensor_id!r}>'


def create(sensor_id, temperature, timestamps):
    u = Sensor(sensor_id=sensor_id, temperature=temperature,
               timestamps=timestamps)
    db_session.add(u)
    db_session.commit()


def fetch():
    list = []
    stmt = select(Sensor).where()
    for sensor in db_session.scalars(stmt):
        list.append({
            "sensor_id": sensor.sensor_id,
            "temperature": sensor.temperature,
            "timestamps": sensor.timestamps
        })
    return list
