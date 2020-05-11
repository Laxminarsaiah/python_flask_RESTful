"""usercntroller"""
import logging.config
from http import HTTPStatus

from flask import Blueprint, request, make_response
from flask.json import jsonify
from flask.views import MethodView

from server.rest.controller.decorators import validate_request
from server.rest.service.user import UserService

USER_BLUEPRINT = Blueprint('user', __name__)
# Preparing log configuration
logging.config.fileConfig(fname='configuration/logging.config',
                          disable_existing_loggers=True)
logger = logging.getLogger('pyweb')


class User(MethodView):
    """User view"""

    @staticmethod
    def create_user():
        """POST method to create user"""
        logger.info("User post method called...")
        data = request.get_json(force=True)
        if 'username' not in data or data['username'] == '':
            return make_response(jsonify({
                'status': 'NOT_ACCEPTABLE',
                'message': 'Username must not be empty'
            })), HTTPStatus.NOT_ACCEPTABLE
        retval, message = UserService.create_user(data)
        if retval == 0:
            return make_response(jsonify({
                'status': 'OK',
                'message': message
            })), HTTPStatus.OK
        else:
            return make_response(jsonify({
                'status': 'INTERNAL_SERVER_ERROR',
                'message': message
            })), HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def get_user():
        """GET method to get user"""
        retval, message = UserService.get_user()
        if retval == 0:
            return make_response(jsonify(message)), HTTPStatus.OK
        else:
            return make_response(jsonify({
                'status': 'INTERNAL_SERVER_ERROR',
                'message': message
            })), HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def update_user():
        """PUT method to update user by name"""
        logger.info("User PUT method called...")
        data = request.get_json(force=True)
        if 'username' not in data or data['username'] == '':
            return make_response(jsonify({
                'status': 'NOT_ACCEPTABLE',
                'message': 'Username must not be empty'
            })), HTTPStatus.NOT_ACCEPTABLE
        retval, message = UserService.update_user(data)
        if retval == 0:
            return make_response(jsonify({
                'status': 'OK',
                'message': message
            })), HTTPStatus.OK
        elif retval == 1:
            return make_response(jsonify({
                'status': 'NOT_FOUND',
                'message': message
            })), HTTPStatus.NOT_FOUND
        else:
            return make_response(jsonify({
                'status': 'INTERNAL_SERVER_ERROR',
                'message': message
            })), HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    def delete_user():
        """DELETE method to update user by name"""
        logger.info("User delete method called...")
        data = request.get_json(force=True)
        if 'username' not in data or data['username'] == '':
            return make_response(jsonify({
                'status': 'NOT_ACCEPTABLE',
                'message': 'Username must not be empty'
            })), HTTPStatus.NOT_ACCEPTABLE
        retval, message = UserService.delete_user(data)
        if retval == 0:
            return make_response(jsonify({
                'status': 'OK',
                'message': message
            })), HTTPStatus.OK
        elif retval == 1:
            return make_response(jsonify({
                'status': 'NOT_FOUND',
                'message': message
            })), HTTPStatus.NOT_FOUND
        else:
            return make_response(jsonify({
                'status': 'INTERNAL_SERVER_ERROR',
                'message': message
            })), HTTPStatus.INTERNAL_SERVER_ERROR


@USER_BLUEPRINT.route("/api/user", methods=['POST'])
@validate_request
def createuser():
    """create user end point"""
    return User.create_user()


@USER_BLUEPRINT.route("/api/user", methods=['GET'])
def getuser():
    """get user end point"""
    return User.get_user()


@USER_BLUEPRINT.route("/api/user", methods=['PUT'])
@validate_request
def updateuser():
    """update user end point"""
    return User.update_user()


@USER_BLUEPRINT.route("/api/user", methods=['DELETE'])
@validate_request
def deleteuser():
    """delete user end point"""
    return User.delete_user()
