class GeocodeProxy:
    """
    Maintains a list of geocoding services,
    exposes the getByAddress functionality
    of the primary service via RESTful API
    """

    def __init__(self, services):
        self.services = services

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










