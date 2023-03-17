from flask import Blueprint, request, jsonify, render_template

tryme = Blueprint('tryme', __name__, url_prefix='/tryme')


@tryme.route('/')
def index():
    return "Hello, tryme!"