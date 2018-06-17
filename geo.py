# Using Python requests and the Google Maps Geocoding API.
#
# References:
#
# https://cloud.google.com/maps-platform/

import requests


def getOrigin(address):
    geoCodingUrl = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address}

    req = requests.get(geoCodingUrl, params=params)
    res = req.json()

    # Choosing the first output
    if "error_message" in res:
        return {"error": res["status"],
                "error_message": res["error_message"]}
    if len(res["results"]) > 0:
        result = res['results'][0]
    else:
        return {"error": "GEOCODE_API_ERROR", "error_message": "Error in Google Api Geocoding. Please try again!"}
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']

    return lat, lng
