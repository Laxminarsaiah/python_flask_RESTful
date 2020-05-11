"""User Service"""
import logging.config
from server.mongoclient import MyMongoClient

# Preparing log configuration
logging.config.fileConfig(fname='configuration/logging.config',
                          disable_existing_loggers=True)
logger = logging.getLogger('pyweb')


class UserService:
    """user service class"""

    @staticmethod
    def create_user(data):
        """POST method to create user"""
        logger.info('In service')
        try:
            db = MyMongoClient().get_client().mymongo
            username = data['username']
            logger.info('Getting user by name: {}'.format(username))
            user = db.user.find_one({'username': username})
            logger.info(user)
            if user is None:
                db.user.insert(data)
                logger.info('User created successfully: {}'.format(username))
                return 0, 'User created successfully.'
            logger.info('User already exists with name: {}'.format(username))
            return 0, 'User already exists'
        except Exception as ex:
            logger.info('Unable to create user: {}'.format(ex))
            raise Exception(ex)

    @staticmethod
    def get_user():
        """GET method to get user"""
        try:
            db = MyMongoClient().get_client().mymongo
            logger.info('Getting user data')
            data = db.user.find({})
            users = []
            for item in data:
                logger.info(item)
                users.append(item)
            return 0, users
        except Exception as ex:
            logger.info('Unable to get user data: {}'.format(ex))
            raise Exception(ex)

    @staticmethod
    def update_user(data):
        """PUT method to update user by name"""
        try:
            db = MyMongoClient().get_client().mymongo
            username = data['username']
            logger.info('Getting user by name: {}'.format(username))
            user = db.user.find_one({'username': username})
            logger.info(user)
            if user is None:
                return 1, 'User not found to update.'
            else:
                db.user.update_one({'username': username}, {'$set': data})
                return 0, 'User updated successfully'
        except Exception as ex:
            logger.info('Unable to delete user {}'.format(ex))
            raise Exception(ex)

    @staticmethod
    def delete_user(data):
        """DELETE method to update user by name"""
        try:
            db = MyMongoClient().get_client().mymongo
            response = db.user.delete_one({'username': data['username']})
            if response.deleted_count == 1:
                return 0, 'User deleted successfully'
            else:
                return 1, 'User not found to delete'
        except Exception as ex:
            logger.info('Unable to delete user {}'.format(ex))
            raise Exception(ex)
