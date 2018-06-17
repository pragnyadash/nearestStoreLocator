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
        return {"error": "OVER_QUERY_LIMIT",
                "error_message": "You have exceeded your daily request quota for this API. We recommend registering for a key at the Google Developers Console: https://console.developers.google.com/apis/credentials?project=_"}
    if len(res) > 0:
        result = res['results'][0]
    else:
        return {"error": "GEOCODE_API_ERROR", "error_message": "Error in Google Api Geocoding. Please try again!"}
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    return lat, lng
