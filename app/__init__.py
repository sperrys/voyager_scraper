import logging
import os

from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config

from .voyager_scraper import api


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(api, url_prefix='/')

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/voyager_scraper.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Voyager Scraper Webserver startup')

    return app
