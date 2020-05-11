"""decorators"""
import logging.config
from functools import wraps
from http import HTTPStatus

import flask
from flask import request, make_response
from werkzeug.exceptions import BadRequest

logging.config.fileConfig(fname='configuration/logging.config',
                          disable_existing_loggers=True)
logger = logging.getLogger('pyweb')


def validate_request(func):
    """validates session"""

    @wraps(func)
    def decorator():
        """decorator"""
        try:
            request.get_json(force=True)
        except BadRequest as ex:
            logger.warning(ex)
            return make_response(flask.jsonify({
                'status': 'BAD_REQUEST',
                'message': 'Request body must not be empty'
            }), HTTPStatus.BAD_REQUEST)
        return func()

    return decorator
