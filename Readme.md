# Overview

This geocoding proxy provides a service for hosting a RESTful
API to retrieve latitude and longitude coordinates for a given address.

Key Features:
* Extensible adapter architecture for multiple third-party geocoding provider support
* Automatic failover from the primary provider to any of the backup providers
* Configurable rate limiting capability (default: ```1 request per second```)
* External configuration file to store API provider secrets (config.ini)
* Error, Debug and Warning logging capabilities
* Built-in web server for luxurious development experience (Flask)


Requirements:
* Python 3.5+


## Installation

1. Get the dependencies with ```pip install``` (may need sudo permissions):

```
pip install -r requirements.txt
```

2. Modify ```config.ini``` to include your geocode API provider credentials
(currently tested with Here.com and Google geocode API)


## Running the tests

Running the unit tests:

```
python3 -m unittest discover -v
```

Will produce the following output:

```
test_failover_to_secondary_service (tests.test_geocode_proxy.TestGeocodeProxy) ... ok
WARNING:root:Unable to parse response from Google API: broken api response
test_primary_service_works (tests.test_geocode_proxy.TestGeocodeProxy) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

This warning is expected, as it signals that the test has succeeded at
simulating a broken API response from the first service to force a
failover to the secondary service.


## Starting the service

Run the service for development with Flask web server (default port ```9999```):

```
python3 geocode_app.py
```


## Using the API

Access the API by navigating to localhost:9999/coordinates/<some street address here>. Example:

Request:
```
http://localhost:9999/coordinates/425+W+Randolph+Chicago
```

Response:

```
{
    "lng": -87.6387699,
    "lat": 41.88449
}
```


## Deployment notes

Flask web server is not designed to be used in production. However, a Flask app is a WSGI application,
so it can be deployed to production [in a variety of ways](http://flask.pocoo.org/docs/0.12/deploying/).
Additional Flask configuration details can be found [here](http://flask.pocoo.org/docs/0.12/config/).

For example, to host this app using uwsgi, use the following command:

```
uwsgi --socket 0.0.0.0:8000 --protocol=http --plugin python35 --manage-script-name --mount /=geocode_app:app
```