class TestResponse:

    def __init__(self):
        self.google_response = {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "425",
                            "short_name": "425",
                            "types": ["street_number"]
                        },
                        {
                            "long_name": "West Randolph Street",
                            "short_name": "W Randolph St",
                            "types": ["route"]
                        },
                        {
                            "long_name": "West Loop Gate",
                            "short_name": "West Loop Gate",
                            "types": ["neighborhood", "political"]
                        },
                        {
                            "long_name": "Chicago",
                            "short_name": "Chicago",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Cook County",
                            "short_name": "Cook County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "Illinois",
                            "short_name": "IL",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        },
                        {
                            "long_name": "60606",
                            "short_name": "60606",
                            "types": ["postal_code"]
                        },
                        {
                            "long_name": "1515",
                            "short_name": "1515",
                            "types": ["postal_code_suffix"]
                        }
                    ],
                    "formatted_address": "425 W Randolph St, Chicago, IL 60606, USA",
                    "geometry": {
                        "location": {
                            "lat": 41.8841621,
                            "lng": -87.6389545
                        },
                        "location_type": "ROOFTOP",
                        "viewport": {
                            "northeast": {
                                "lat": 41.88551108029151,
                                "lng": -87.63760551970849
                            },
                            "southwest": {
                                "lat": 41.88281311970851,
                                "lng": -87.64030348029149
                            }
                        }
                    },
                    "partial_match": True,
                    "place_id": "ChIJK7itjMcsDogRbvEVSJYgYT8",
                    "types": ["street_address"]
                }
            ],
            "status": "OK"
        }
        self.here_response = {
            "Response": {
                "MetaInfo": {
                    "Timestamp": "2018-02-10T13:14:42.416+0000"
                },
                "View": [
                    {
                        "_type": "SearchResultsViewType",
                        "ViewId": 0,
                        "Result": [
                            {
                                "Relevance": 1.0,
                                "MatchLevel": "houseNumber",
                                "MatchQuality": {
                                    "City": 1.0,
                                    "Street": [
                                        0.9
                                    ],
                                    "HouseNumber": 1.0
                                },
                                "MatchType": "pointAddress",
                                "Location": {
                                    "LocationId": "NT_Opil2LPZVRLZjlWNLJQuWB_0ITN",
                                    "LocationType": "point",
                                    "DisplayPosition": {
                                        "Latitude": 41.88432,
                                        "Longitude": -87.6387699
                                    },
                                    "NavigationPosition": [
                                        {
                                            "Latitude": 41.88449,
                                            "Longitude": -87.6387699
                                        }
                                    ],
                                    "MapView": {
                                        "TopLeft": {
                                            "Latitude": 41.8854442,
                                            "Longitude": -87.6402799
                                        },
                                        "BottomRight": {
                                            "Latitude": 41.8831958,
                                            "Longitude": -87.6372599
                                        }
                                    },
                                    "Address": {
                                        "Label": "425 W Randolph St, Chicago, IL 60606, United States",
                                        "Country": "USA",
                                        "State": "IL",
                                        "County": "Cook",
                                        "City": "Chicago",
                                        "District": "West Loop",
                                        "Street": "W Randolph St",
                                        "HouseNumber": "425",
                                        "PostalCode": "60606",
                                        "AdditionalData": [
                                            {
                                                "value": "United States",
                                                "key": "CountryName"
                                            },
                                            {
                                                "value": "Illinois",
                                                "key": "StateName"
                                            },
                                            {
                                                "value": "Cook",
                                                "key": "CountyName"
                                            },
                                            {
                                                "value": "N",
                                                "key": "PostalCodeType"
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                ]
            }
        }
