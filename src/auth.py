import os
import pathlib

import requests
from flask import session, abort, redirect, request, Blueprint
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

auth = Blueprint('auth', __name__, url_prefix='/auth') 
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "10" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = "615107743513-808o8ccs2o1b5j1p7bnu8v3ojlkkb986.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/auth/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@auth.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    # if not session["state"] == request.args["state"]:
    #     abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    session['id_info'] = id_info
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    
    return redirect("/auth/protected_area")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@auth.route("/")
def index():
    return "Hello World <a href='/auth/login'><button>Login</button></a>"


@auth.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['id_info']['email']}! <br/> <a href='/auth/logout'><button>Logout</button></a>"