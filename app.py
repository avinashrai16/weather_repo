from flask import Flask, render_template, request
import requests
#import json

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=['POST','GET'])
def get_watherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
          "q":request.form["city"],
          "appid":request.form["appid"],
          "units":request.form["units"]
          }
    weather_data = requests.get(url,params=params)
    #print(weather_data.status_code)
    #weather_data_dict = json.loads(str(weather_data.json()))
    #temp_min = weather_data.json()["temp_min"]
    #temp_max = weather_data_dict["temp_max"]
    #print(temp_min)
    return f"temp_range for {request.form['city']} is {weather_data.json()} "


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")

