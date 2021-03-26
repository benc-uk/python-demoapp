from flask import Flask

app = Flask(__name__)

from app import views  # noqa: E402,F401
from app import apis  # noqa: E402,F401
