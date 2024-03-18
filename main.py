import requests
import datetime as dt
from flask import Flask, render_template, request
from types import MethodType
from weatherCalculation import kelvin_to_celsius, kelvin_to_farenheit

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = <Your-API-Key>

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/clicked')
def weather():
  city = str(request.args.get('city'))
  url = BASE_URL + "appid=" + API_KEY + "&q=" + city
  response = requests.get(url).json();
  temp_kelvin = response['main']['temp']
  temp_celsius = kelvin_to_celsius(temp_kelvin)
  temp_farenheit = kelvin_to_farenheit(temp_celsius)

  description = response['weather'][0]['description']
  print(description)
  return render_template('weatherReport.html', 
      city = city, 
      celsius = round(temp_celsius, 2), farenheit =     
      round(temp_farenheit, 2), 
      description = description)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
