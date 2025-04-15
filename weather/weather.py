import requests
import pandas as pd
from datetime import datetime
import os
import argparse

basic_url = "https://wttr.in/"

def get_weather_data(city):
    url = f"{basic_url}{city}?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    weather_data = response.json()
    return weather_data

def parse_weather_data(weather_data, city):
    curr_condition = weather_data["current_condition"][0]
    pressure_gpa = curr_condition["pressure"]
    pressure_mmhg = round(int(pressure_gpa)* 0.750062, 2)
    currernt_condition_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "city": city,
        "temperature_C": curr_condition["temp_C"],
        "feels_like_C": curr_condition["FeelsLikeC"],
        "weatherDescription": curr_condition["weatherDesc"][0]["value"],
        "humidity": curr_condition["humidity"],
        "pressure_mmhg": pressure_mmhg,
        "pressure_gpa": pressure_gpa,
        
    }       
    return currernt_condition_data

def save_to_csv(weather_data, city):
    weather_data = parse_weather_data(weather_data, city)
    file_name = f"{city}_weather.csv"
    df = pd.DataFrame([weather_data])
    
    if os.path.exists(file_name):
        df.to_csv(file_name, mode='a', header=False, index=False)
    else:
        df.to_csv(file_name, index=False)
    

def parse_arguments():
    parser = argparse.ArgumentParser(description='Отримати погоду для вказаного міста')
    parser.add_argument('city', type=str, help='Назва міста (наприклад: kyiv, london, tokyo)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    weather_data = get_weather_data(args.city)
    save_to_csv(weather_data, args.city)

