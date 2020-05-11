"""user view"""
import requests
from flask import Blueprint, render_template
from flask.views import View

DASHBOARD_BLUEPRINT = Blueprint('dashboard', __name__)


class Dashboard(View):
    """home controller"""

    def dispatch_request(self):
        """dispatch request"""
        response = requests.get('http://127.0.0.1:5000/api/user')
        userdata = response.json()
        return render_template('dashboard/dashboard.html', userdata=userdata)


class Register(View):
    """home controller"""
    def dispatch_request(self):
        """dispatch request"""
        return render_template('register/register.html')


DASHBOARD_VIEW = Dashboard.as_view('home_page')
REG_VIEW = Register.as_view('reg_page')

# add Rules for API Endpoints
DASHBOARD_BLUEPRINT.add_url_rule(
    '/',
    view_func=DASHBOARD_VIEW
)

# add Rules for API Endpoints
DASHBOARD_BLUEPRINT.add_url_rule(
    '/registerform',
    view_func=REG_VIEW
)
