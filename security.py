from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    '''
    This is a function that gets called when a user calls the /auth endpoint
    with their username and password.
    :param username: user's username in string format.
    :param password: User's un-encrypted password in string format.
    :return: A UserModel object if authentication was successful, None otherwise.
    '''

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    return None

def identity(payload):
    '''
    Function that gets called when user has already authenticated, and Flask-JWT token
    verfied their authorization header is correct.
    :param payload: A dictionary with 'identity' key, which is user's id
    :return: A UserModel object
    '''

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

