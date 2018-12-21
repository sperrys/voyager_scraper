import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
