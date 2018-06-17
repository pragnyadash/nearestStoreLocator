import math
import csv
from geo import getOrigin


def getNearestStores(addr, unit=None, output=None):
    """

    :param addr: address of the origin to which nearest store needs to be found
    :param unit: optional argument for distance unit
    :param output: optional argument for format of output
    :return: formatted address of the nearest store
    """
    closest = None
    store = None
    origin = getOrigin(addr)
    if "error" in origin:
        return origin
    originLat, originLng = origin[0], origin[1]
    try:
        filename = 'store-locations.csv'
        csvfile = open(filename, 'r')
        stores = csv.DictReader(csvfile)
    except:
        return {"error": "Cannot read store location file."}
    for row in stores:
        try:
            row['Latitude']
            row['Longitude']
        except:
            pass
        else:
            if row['Latitude'] not in [None, '', 'None'] and row['Longitude'] not in [None, '', 'None']:
                destination = (float(row['Latitude']), float(row['Longitude']))
                dist = distance((float(originLat), float(originLng)), destination, unit)
                if "error" in dist:
                    return dist
                if closest is None:
                    closest = round(dist, 2)
                    store = row
                elif closest > dist:
                    closest = round(dist, 2)
                    store = row
    csvfile.close()
    return formatAddr(store, closest, unit, output)


def getStores():
    """"""
    stores = []
    try:
        filename = 'store-locations.csv'
        csvfile = open(filename, 'r')
        reader = csv.DictReader(csvfile)
    except:
        return None
    else:
        for row in reader:
            stores.append(row)
    return stores


def distance(start, end, unit=None):
    #
    # References:
    #
    # https://www.movable-type.co.uk/scripts/latlong.html
    """
    :param start: tuple of latitude longitude starting position
    :param end: tuple of latitude longitude ending position
    :return:
    """
    if type(start) == tuple and type(end) == tuple:
        latS, lonS = start
        latE, lonE = end
        if type(latS) != float or type(lonS) != float or type(latE) != float or type(lonE) != float:
            return {"error": "INCORRECT_LATLNG_TYPE",
                    "error_message": "Cannot find distance between two lat lng which are not floating point numbers"}
    else:
        return {"error": "INCORRECT_DESTORG_INPUT",
                "error_message": "Need a tuple of lat lng for origin and destination addresses."}

    rad = 3959
    if unit:
        if unit == "km":
            rad = 6371

    delLat = math.radians(latE - latS)
    delLng = math.radians(lonE - lonS)
    a = math.sin(delLat / 2) * math.sin(delLat / 2) + \
        math.cos(math.radians(latS)) * math.cos(math.radians(latE)) * \
        math.sin(delLng / 2) * math.sin(delLng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = rad * c
    return d


def formatAddr(address, distance, unit, output):
    """

    :param address: json formatted row from csv file
    :param distance: distance from origin in mi/km
    :param unit: unit expected by user
    :param output: output format expected by user
    :return: formatted address of the store location
    """
    addr = ""
    if unit and unit in ["km", "mi"]:
        d = str(distance) + " " + unit
    else:
        d = str(distance) + " " + "mi"
    if output and output == "json":
        if type(address) != dict:
            return {"error": "INCORRECT_ADDRESS",
                    "error_message": "Improperly formatted address input. Please provide a json formatted address."}

        addr = address
        addr["Distance"] = d
    else:
        if type(address) != dict:
            return {"error": "INCORRECT_ADDRESS",
                    "error_message": "Improperly formatted address input. Please provide a json formatted address."}
        if "Store Name" in address:
            addr += address["Store Name"] + '\n'
        if "Address" in address:
            addr += address["Address"] + ', '
        if "City" in address:
            addr += address["City"] + ', '
        if "County" in address:
            addr += address["County"] + ', '
        if "Zip Code" in address:
            addr += address["Zip Code"]
        addr += '\n' + d

    return addr
