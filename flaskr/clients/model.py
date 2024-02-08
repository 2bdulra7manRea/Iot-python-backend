from sqlalchemy import Column, Integer, String, select, LargeBinary
from ..db.database import Base, db_session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=True)
    password = Column(LargeBinary, unique=False)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password


def createUser(name, email, password):
    u = User(name, email, password=password)
    db_session.add(u)
    db_session.commit()


def fetch():
    list = []
    stmt = select(User).where()
    for user in db_session.scalars(stmt):
        list.append({
            "name": user.name,
            "email": user.email,
        })
    return list


def fetch_user(email: str):
    list = []
    stmt = select(User).where(User.email == email)
    print(stmt)
    for user in db_session.scalars(stmt):
        list.append({
            "email": user.email,
            "password": user.password,
            "id": user.id
        })

    if (list and list[0]):
        return list[0]

    return None
