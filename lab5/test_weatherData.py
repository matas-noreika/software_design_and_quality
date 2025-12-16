# Programmer: Matas Noreika
# Purpose: unit test for weatherData class

import unittest
from WeatherDataClass import WeatherData

class TestWeatherData(unittest.TestCase):

    def test_summeraise(self):
        print('test_summeraise')

        data1 = WeatherData(25, 50, 1)
        
        print(data1.summeraise)
        self.assertEqual(data1.summeraise, '25 50 1')
    
    def test_collectData(self):
        print('test_collectWeatherData')

        data1 = WeatherData(20, 10, 2)

        data1.collectWeatherData

        self.assertNotEqual(data1.summeraise, '20 10 1')

if __name__ == '__main__':
    unittest.main()
