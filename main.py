"""
  Find Store
  find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.
Usage:
  find_store --address=<address>
  find_store --address=<address> [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address=<address>  Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]
"""

from docopt import docopt
from getstore import *


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.6.2')
    if arguments:
        if "--units" in arguments:
            units = arguments["--units"]
            if units not in ["mi", "km"]:
                print("Unidentified unit. Please use mi/km.")
                units = None
        else:
            units = None
        if "--output" in arguments:
            output = arguments["--output"]
            if output not in ["text", "json"]:
                print("Unidentified output. Please use text/json.")
                output = None
        else:
            output = None
        if "--address" in arguments:
            address = arguments["--address"]
            print(getNearestStores(address, units, output))
        if "--zip" in arguments:
            zip = arguments["--zip"]
            print(getNearestStores(zip, units, output))

    else:
        print("Please provide arguments")
    # getAllStores(arguments[1])
