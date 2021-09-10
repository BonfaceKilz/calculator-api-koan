"""Entry point from spinning up flask"""
import os

from typing import Dict
from typing import Union
from flask import Flask
from app.api.discounts import discounts


def create_app(config: Union[Dict, str, None] = None) -> Flask:
    """Create a new flask object"""
    app = Flask(__name__)
    # Load default configuration
    app.config.from_object("app.settings")

    # Load environment configuration
    if "GN3_CONF" in os.environ:
        app.config.from_envvar('STORE_CONF')

    # Load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith(".py"):
            app.config.from_pyfile(config)

    app.register_blueprint(discounts, url_prefix="/api/v1/bill")
    return app
