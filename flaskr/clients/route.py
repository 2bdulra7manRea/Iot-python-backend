
from flask import Blueprint, request, jsonify
from .client import Client, jwt_guard

client_route = Blueprint("client", __name__, url_prefix="/auth")


@client_route.route("/client")
@jwt_guard
def getClients():
    client = Client()
    results = client.getClients()
    return jsonify(results)


@client_route.post('/login')
def login():
    client = Client()
    return client.login(request.get_json())


@client_route.post('/register')
def register_new_account():
    client = Client()
    return client.register(request.get_json())
