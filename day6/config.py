

class baseconfig():
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'


class localdev(baseconfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
    SECRET_KEY = 'shhh_its secret'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'


class prod(baseconfig):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'
    # SECRET_KEY = get.env
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'