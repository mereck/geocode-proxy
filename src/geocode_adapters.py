import logging
from urllib import parse
from src.geocode_helper import GeocodeServiceHelper


class GeocodeServiceInterface:
    """
    Represents an external provider of geocode data
    """
    def __init__(self, config, is_primary):
        self.config = config
        self.is_primary = is_primary

    def get_by_address(self, address):
        """
        Looks up lat and lng coordinates of a location by address
        :param address: string with a physical address
        :return: results of transform
        """
        pass

    def transform(self, result):
        """
        Transforms the external api results to uniform output
        :param result: api-specific location query result
        :return: dict of lat, lng coordinates
        """
        pass

    def toggle_is_primary(self):
        self.is_primary = not self.is_primary


class GoogleAdapter (GeocodeServiceInterface):
    """
    Google geocode service adapter, responsible for transforming the input to and output from Google geocode API
    """

    def __init__(self, config, is_primary):
        self.config = config["Google"]
        self.is_primary = is_primary

    def get_by_address(self, address):
        c = self.config
        url = c["Url"] + parse.urlencode({"Key": c["Key"], c["QueryParam"]: address})
        result = GeocodeServiceHelper.invoke_api(url, "Google Geocode")
        return self.transform(result)

    def transform(self, result):
        loc = GeocodeServiceHelper.find("location", result)
        if loc:
            return loc["location"]

        else:
            logging.warning("Unable to parse response from Google API: {}", result)


class HereAdapter (GeocodeServiceInterface):
    """
    Here.com geocode service adapter, responsible for transforming the input to and output from Here geocode API
    """

    def __init__(self, config, is_primary):
        self.config = config["Here"]
        self.is_primary = is_primary

    def get_by_address(self, address):
        c = self.config
        url = c["Url"] + parse.urlencode({"app_id": c["App_Id"], "app_code": c["App_Code"], c["QueryParam"]: address})
        result = GeocodeServiceHelper.invoke_api(url, "Here Geocode")
        return self.transform(result)

    def transform(self, result):
        loc = GeocodeServiceHelper.find("NavigationPosition", result)

        try:
            n = loc["NavigationPosition"]
            return {"lng": n[0]["Longitude"], "lat": n[0]["Latitude"]}
        except KeyError:
            logging.warning("Unable to parse response from Here API: {}".format(result))