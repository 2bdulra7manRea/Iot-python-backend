from .model import createUser, fetch, fetch_user
import bcrypt
import jwt
from datetime import datetime
from flask import request
from functools import wraps
from ..config import secret_key

JWT_SECRET = secret_key


class PasswordManager:

    def hash_password(self, password: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password=password.encode(), salt=salt)

    def verify_password(self, hash_password, password: str) -> bool:
        return bcrypt.checkpw(password=password.encode(), hashed_password=hash_password)


class Auth:

    def generate_token(self, payload) -> str:
        return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    def verify_token(self, token):
        return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])


class Client:

    def login(self, data):
        user = fetch_user(data['email'])

        if (user is None):
            return {"message": "not found"}, 404

        passwordManager = PasswordManager()

        if (not passwordManager.verify_password(user['password'], data['password'])):
            return {"message": "email/password is not correct"}, 400

        auth = Auth()
        token = auth.generate_token(
            {"email": user['email'], "date": datetime.now().__str__()})
        return {"access_token": token}

    def register(self, data):

        user = fetch_user(data['email'])

        if (user is not None):
            return {"message": "User already exists"}, 400

        passwordManager = PasswordManager()
        password = data["password"]
        hash = passwordManager.hash_password(password=password)
        createUser(name=data['name'],
                   email=data['email'], password=hash)
        auth = Auth()
        token = auth.generate_token(
            {"email": data['email'], "date": datetime.now().__str__()})
        return {"access_token": token}

    def getClients(self):
        return fetch()


def jwt_guard(f):
    @wraps(f)
    def alpha(*arg, **args):

        try:
            token = None
            if "Authorization" in request.headers:
                token = request.headers['Authorization'].split(' ')[1]

                if (not token):
                    return {"message": "Authentication Token is missing!"}, 401
            else:
                return {"message": "Authentication Token is missing!"}, 401

            auth = Auth()
            token_payload = auth.verify_token(token)

            email = token_payload['email']
            if (not email):
                return {"message": "Authentication Token is invalid!"}, 401

            user = fetch_user(email)

            if (user is None):

                return {"message": "Authentication Token is invalid!"}, 401

            val = f(*arg, **args)
            return val
        except:
            return {"message": "Authentication Token is invalid!"}, 401

    return alpha
