import logging
import requests
from xml.etree import ElementTree

# URL's
WEATHER_URL = "http://w1.weather.gov/xml/current_obs/display.php"
FORECAST_URL = "http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php"


class Weather(object):
    def __init__(self, scheduler, zip, station):
        self._zip = zip
        self._station = station

        self.cur_temp = 0.0
        self.high_temp = 0.0
        self.low_temp = 0.0
        self.cur_weather_desc = ""
        #self.wind_mph = 0.0

        self.update()

        # Update weather every 15 minutes
        scheduler.add_job(self.update, 'cron', minute='*/15')

    def update(self):
        logging.info("Updating weather")

        weather_req = requests.get(WEATHER_URL, params={'stid': self._station})
        if weather_req.ok:
            weather = ElementTree.fromstring(weather_req.content)
            #self.cur_temp = float(weather.find("temp_f").text)
            #logging.info("Current temperature %1.1f" % self.cur_temp)
            #self.cur_temp = float(weather.find("wind_mph").text)
            #logging.info("Current temperature %1.1f" % self.cur_temp)
            self.cur_weather_desc = (weather.find("weather").text)
            logging.info("Current Weather Description %s" % self.cur_weather_desc)

        forecast_req = requests.get(FORECAST_URL, params={'zipCodeList': self._zip, 'format': '24 hourly', 'numDays': 1})
        if forecast_req.ok:
            forecast = ElementTree.fromstring(forecast_req.content)
            #self.high_temp = float(forecast.find(".//temperature[@type='maximum']/value[1]").text)
            #self.low_temp = float(forecast.find(".//temperature[@type='minimum']/value[1]").text)
            #logging.info("High temperature %1.1f, Low temperature %1.1f" % (self.high_temp, self.low_temp))
