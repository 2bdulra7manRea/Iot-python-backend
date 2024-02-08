from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from ..config import database_url


DATABASE_URL = database_url

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from ..clients.model import User
    from ..sensor.model import Sensor
    from ..sensor.register_model import SensorRegister
    Base.metadata.create_all(bind=engine)
