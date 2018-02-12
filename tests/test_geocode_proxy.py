import unittest
from .test_response_data import TestResponse
from src.geocode_helper import GeocodeServiceHelper
from src.geocode_proxy import GeocodeProxy
from src.geocode_adapters import GoogleAdapter, HereAdapter


class TestGeocodeProxy (unittest.TestCase):

    @staticmethod
    def mock_api(url, name):
        tr = TestResponse()

        if name == "Google Geocode":
            return tr.google_response
        else:
            return tr.here_response

    def setUp(self):
        self.mock_helper = GeocodeServiceHelper()

        self.mock_helper.invoke_api = self.mock_api

        config = self.mock_helper.get_config("config.test.ini")

        self.gcp = GeocodeProxy([GoogleAdapter(config, True, self.mock_helper.invoke_api),
                                 HereAdapter(config, False, self.mock_helper.invoke_api)])

    def test_primary_service_works(self):
        services = self.gcp.services
        self.assertTrue(services[0].is_primary)
        self.assertTrue(not services[1].is_primary)

        assert self.gcp.get_coordinates_by_address("425 W Randolph Chicago") == {'lng': -87.6389545, 'lat': 41.8841621}

        self.assertTrue(services[0].is_primary)
        self.assertTrue(not services[1].is_primary)

    def test_failover_to_secondary_service(self):
        services = self.gcp.services
        self.assertTrue(services[0].is_primary)
        self.assertTrue(not services[1].is_primary)

        self.gcp.services[0].api_helper = lambda x, y: "broken api response"

        res = self.gcp.get_coordinates_by_address("425 W Randolph Chicago")
        self.assertTrue(res == {'lng': -87.6387699, 'lat': 41.88449})

        self.assertTrue(not services[0].is_primary)
        self.assertTrue(services[1].is_primary)


if __name__ == "main":
    unittest.main(verbosity=2)

