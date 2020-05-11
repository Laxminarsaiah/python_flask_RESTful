"""__init__"""
import json
from datetime import datetime

from bson import ObjectId
from flask import Flask
from server.rest.controller import user
from server.views import userview

app = Flask(__name__)

app.register_blueprint(user.USER_BLUEPRINT)
app.register_blueprint(userview.DASHBOARD_BLUEPRINT)


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

if __name__ == '__main__':
    # app.debug = True
    # DEBUG_TOOLBAR_ENABLED = True
    app.run()
