import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    
    def test_city_contry(self):
        city_contry = get_city_country('Shanghai','China')
        self.assertEqual(city_contry,'Shanghai, China')
        
unittest.main()
        