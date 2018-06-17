# nearestStoreLocator
Read a csv file with store locations and give back nearest store for a given location

The main.py file is where the program starts and the usage is as follows:
python3 main.py --zip="94586" --units="km"
python3 main.py --address="1770 Union St, San Francisco, CA 94123" --output="json"

The expected parameters:
 - Zip/Address
 - Ouput (optional, default = text) json/text
 - Unit (optional, default = mi) mi/km
 
 The main function calls the getNearestStore which then parses through the csv file in order to get all store locations. It calls the google geo.py client to get lat/lng values for the given address which is the origin. It maintains two variables, store and closest(distance to a store). For each store in the csv, we send the origin lat/lng and the dest store lat/lng to the distance function. This calculates the ariel distance between the two points. If the existing distance is shorter than what we have stored in our variables, we update them. By the end of this loop, we have a store row and distance between origin and store. We send this to format address which then formats it as per given arguments.
 
 Assumptions/Caveats:
 1- We calculate ariel distance here and not the actual map distance to keep things simpler. We can use google map api to get the actual road distance as well or use maps to write an algorithm that does something similar. 
 
 2- The test.py file can be run as python3 test.py. This only tests for the functions specific to the project and not the google api client. 
 
 3- The api client doesnt have an api key which rate limits it, so if there are any errors thrown on rate limit, it needs to be rerun. 
