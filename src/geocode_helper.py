import configparser
import json
import logging
from urllib import request
from urllib.error import URLError


class GeocodeServiceHelper:
    """
    Various static utility methods
    """

    @staticmethod
    def get_config():
        """
        Utility method for loading configuration from a file
        :return: dict with config data
        """

        config = configparser.ConfigParser()
        try:
            config.read("config.ini")
            return config
        except FileNotFoundError as ex:
            logging.error("problem accessing config.ini file: {}".format(ex))
            raise

    @staticmethod
    def invoke_api(url, name):
        """
        Utility method for querying external geocoding api
        :param url: api url with query and secrets
        :param name: name of the api
        :return: dict with response data
        """

        try:

            with request.urlopen(url) as response:
                logging.info("Getting data from {} API".format(name))
                res = json.loads(response.read().decode(response.headers.get_content_charset('utf-8')))
                return res

        except (TimeoutError, URLError) as e:
            if hasattr(e, 'reason'):
                logging.warning('We failed to reach a server.')
                logging.warning('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                logging.warning('The server could not fulfill the request.')
                logging.warning('Error code: ', e.code)

            logging.warning("Error getting data from {} API".format(name))
            return

    @staticmethod
    def find(needles, haystack):
        """
        Finds all instances of a key in nested dictionary/list structure
        inspired by https://stackoverflow.com/a/14049167
        :param needles: keys to find
        :param haystack: dict to search
        :return: generator of matches
        """
        found = {}
        if type(needles) != type([]):
            needles = [needles]

        if type(haystack) == type(dict()):
            for needle in needles:
                if needle in haystack.keys():
                    found[needle] = haystack[needle]
                elif len(haystack.keys()) > 0:
                    for key in haystack.keys():
                        result = GeocodeServiceHelper.find(needle, haystack[key])
                        if result:
                            for k, v in result.items():
                                found[k] = v
        elif type(haystack) == type([]):
            for node in haystack:
                result = GeocodeServiceHelper.find(needles, node)
                if result:
                    for k, v in result.items():
                        found[k] = v
        return found