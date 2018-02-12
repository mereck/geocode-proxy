import logging
import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api, Resource, abort

from src.geocode_adapters import GoogleAdapter, HereAdapter
from src.geocode_helper import GeocodeServiceHelper
from src.geocode_proxy import GeocodeProxy

import argparse

parser = argparse.ArgumentParser(description='Geocode Proxy App')

parser.add_argument('--debug', type=int, help='debug mode, default: 1', default=1)
parser.add_argument('--log-level', type=str, help='log level, default: debug', default='debug')
parser.add_argument('--port', type=int, help='port, default: 9999', default=9999)
parser.add_argument('--config-file', type=str, help='config file, default: config.ini', default='config.ini')


args = parser.parse_args()

app = Flask(__name__)
api = Api(app)
config = GeocodeServiceHelper.get_config(args.config_file)
api_helper = GeocodeServiceHelper.invoke_api
gcp = GeocodeProxy([GoogleAdapter(config, is_primary=False, api_helper=api_helper),
                    HereAdapter(config, is_primary=True, api_helper=api_helper)])
limiter = Limiter(
    app,
    key_func=get_remote_address
    # default_limits=["2000 per day", "500 per hour"]
)


class Coordinates(Resource):

    decorators = [limiter.limit("1/second")]

    def get(self, address):
        return gcp.get_coordinates_by_address(address) or abort(503,
                                                                message="We are terribly sorry, our geocoding "
                                                                        "services are currently unavailable. "
                                                                        "Please try again later.")


logging.basicConfig(filename='{}.log'.format(args.log_level), level=getattr(logging, args.log_level.upper()))

api.add_resource(Coordinates, '/coordinates/<string:address>')

if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    print("Starting Geocode Proxy App with {} and log file {}.log".format(args, args.log_level))

if __name__ == '__main__':
    app.run(debug=args.debug, port=args.port)
