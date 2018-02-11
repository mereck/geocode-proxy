import logging
from flask import Flask
from flask_restful import Resource, Api, abort
from src.geocode_helper import GeocodeServiceHelper
from src.geocode_adapters import GoogleAdapter, HereAdapter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


class GeocodeProxy:
    """
    Maintains a list of geocoding services,
    exposes the getByAddress functionality
    of the primary service via RESTful API
    """

    def __init__(self):
        # todo: change file and level based on global environment config
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)
        self.config = GeocodeServiceHelper.get_config()
        self.services = [GoogleAdapter(self.config, False), HereAdapter(self.config, True)];

    def get_coordinates_by_address(self, address):

        """
        :param address:
        :return:
        """

        for service in [s for s in self.services if s.is_primary]:
            result = service.get_by_address(address)
            if result:
                return result

        for i, service in enumerate(self.services):
            if not service.is_primary:
                result = service.get_by_address(address)
                if result:
                    service.toggle_is_primary()
                    return result
            else:
                service.toggle_is_primary()


app = Flask(__name__)
api = Api(app)
gcp = GeocodeProxy()

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


api.add_resource(Coordinates, '/coordinates/<string:address>')

if __name__ == '__main__':
    app.run(debug=True, port=9999)








