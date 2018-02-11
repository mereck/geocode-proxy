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

1. Get the dependencies with ```pip install```:

```
pip install -r requirements.txt
```

2. Modify config.ini to include your geocode API provider credentials
(currently tested with Here.com and Google geocode API)

## Starting the service

Run the service for development with Flask web server (default port ```9999```):

```
python src\geocode_proxy.py
```

## Using the API

Access the API by navigating to localhost:9999/coordinates/<some street address here>. Example:

Request:
```
http://localhost:9999/coordinates/116th%20St%20&%20Broadway,%20New%20York,%20NY%2010027
```

Response:

```
{
    "lat": 40.80798,
    "lng": -73.96381
}
```

## Deployment notes

Flask web server is not designed to be used in production. However, a Flask app is a WSGI application,
so it can be deployed to production [in a variety of ways] (http://flask.pocoo.org/docs/0.12/deploying/).