from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from housing_service.auth import login_required
from housing_service.db import get_db

bp = Blueprint('rentals', __name__)