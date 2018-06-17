import unittest
from getstore import *

class TestMethods(unittest.TestCase):

    def test_getNearestStores(self):
        import time
        res = getNearestStores("94123")
        self.assertEqual(res,
                         "San Francisco West" + "\n" + "2675 Geary Blvd, San Francisco, San Francisco County, 94118-3400" + "\n" + "1.45 mi")

        res = getNearestStores("94587", "km")
        self.assertEqual(res, "Hayward" + "\n" + "2499 Whipple Rd, Hayward, Alameda County, 94544-7807" + "\n" + "2.12 km")

        time.sleep(15)
        res = getNearestStores("94587", "mi")
        self.assertEqual(res,
                         "Hayward" + "\n" + "2499 Whipple Rd, Hayward, Alameda County, 94544-7807" + "\n" + "1.32 mi")

        res = getNearestStores("94587", "mi", "json")
        self.assertEqual(res["Distance"], "1.32 mi")
        self.assertEqual(res["Address"], "2499 Whipple Rd")
        self.assertEqual(res["City"], "Hayward")
        self.assertEqual(res["Store Name"], "Hayward")
        self.assertEqual(res["County"], "Alameda County")
        self.assertEqual(res["Zip Code"], "94544-7807")

        time.sleep(15)
        res = getNearestStores("94587", "json", "mi")
        self.assertEqual(res,
                         "Hayward" + "\n" + "2499 Whipple Rd, Hayward, Alameda County, 94544-7807" + "\n" + "1.32 mi")

        res = getNearestStores("1770 Union St, San Francisco, CA 94123")
        self.assertEqual(res,
                         "San Francisco West" + "\n" + "2675 Geary Blvd, San Francisco, San Francisco County, 94118-3400" + "\n" + "1.48 mi")

        time.sleep(15)
        res = getNearestStores("1770 Union St, San Francisco, CA 94123", "km")
        self.assertEqual(res,
                         "San Francisco West" + "\n" + "2675 Geary Blvd, San Francisco, San Francisco County, 94118-3400" + "\n" + "2.39 km")

        res = getNearestStores("1770 Union St, San Francisco, CA 94123", "km", "text")
        self.assertEqual(res,
                         "San Francisco West" + "\n" + "2675 Geary Blvd, San Francisco, San Francisco County, 94118-3400" + "\n" + "2.39 km")

        time.sleep(15)
        res = getNearestStores("1770 Union St, San Francisco, CA 94123", "mi", "json")
        self.assertEqual(res["Distance"], "1.48 mi")
        self.assertEqual(res["Address"], "2675 Geary Blvd")
        self.assertEqual(res["City"], "San Francisco")
        self.assertEqual(res["Store Name"], "San Francisco West")
        self.assertEqual(res["County"], "San Francisco County")
        self.assertEqual(res["Zip Code"], "94118-3400")

        res = getNearestStores("1770 Union St, San Francisco, CA 94123", "kmss", "jsonn")
        self.assertEqual(res,
                         "San Francisco West" + "\n" + "2675 Geary Blvd, San Francisco, San Francisco County, 94118-3400" + "\n" + "1.48 mi")

    def test_distance(self):
        res = distance("x", "y")
        self.assertEqual(res["error"], 'INCORRECT_DESTORG_INPUT')
        res = distance("x", "y", "mi")
        self.assertEqual(res["error"], 'INCORRECT_DESTORG_INPUT')
        res = distance(("x1", "y1"), ("x2", "y2"), "mi")
        self.assertEqual(res["error"], 'INCORRECT_LATLNG_TYPE')
        res = distance(("45.0521539", "-93.36485"), ("46.808614", "-92.1681479"), "mi")
        self.assertEqual(res["error"], 'INCORRECT_LATLNG_TYPE')
        res = distance((45.0521539, -93.36485), (46.808614, -92.1681479), "mi")
        self.assertEqual(res, 134.30033185125887)

    def test_formatAddr(self):
        res = formatAddr("address", 3.41, "mi", "json")
        self.assertEqual(res["error"], 'INCORRECT_ADDRESS')

        res = formatAddr({"Address":"123 H Street", "City": "XYZ", "Zip Code":"34432"}, 3.41, "mi", "text")
        self.assertEqual(res, "123 H Street, XYZ, 34432" + "\n3.41 mi")

        res = formatAddr({"Address": "123 H Street", "City": "XYZ", "Zip Code": "34432"}, 3.41, "kms", "json")
        self.assertEqual(res["Distance"], "3.41 mi")

        res = formatAddr({"Address": "123 H Street", "City": "XYZ", "Zip Code": "34432"}, 3.41, "km", "json")
        self.assertEqual(res["Distance"], "3.41 km")


if __name__ == '__main__':
    unittest.main()