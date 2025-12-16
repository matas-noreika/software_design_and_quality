import random
class WeatherData:

    def __init__(self, airTemp, windSpeed, windDirection):
        self.airTemp = airTemp
        self.windSpeed = windSpeed
        self.windDirection = windDirection

    def collectWeatherData():
        self.airTemp = random.randint(20,30)
        self.windSpeed = random.randint(5,100)
        self.windDirection = random.randint(0, 3)
    
    @property
    def summeraise(self):
        return '{} {} {}'.format(self.airTemp, self.windSpeed, self.windDirection)

