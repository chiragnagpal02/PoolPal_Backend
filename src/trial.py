from flask import Blueprint, request, jsonify

tryme = Blueprint('tryme', __name__, url_prefix='/tryme')


@tryme.route('/')
def index():
    return '<h1>Hello, tryme!</h1>'