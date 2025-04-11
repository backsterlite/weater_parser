import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import argparse

def plot_weather_data(city: str):
    filename = f"{city.lower()}_weather.csv"
    file_path = Path(filename)

    if not file_path.exists():
        print(f"File {filename} not found.")
        return

    # Читання CSV
    df = pd.read_csv(file_path)

    # Об'єднання дати й часу в один datetime-стовпчик
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])

    # Побудова графіків
    plt.figure(figsize=(12, 6))
    plt.plot(df["datetime"], df["temperature_C"], marker='o', label="Temperature (°C)")
    plt.plot(df["datetime"], df["feels_like_C"], marker='x', linestyle='--', label="Feels Like (°C)")
    plt.plot(df["datetime"], df["pressure_mmhg"], marker='s', linestyle=':', label="Pressure (mmHg)")
    plt.plot(df["datetime"], df["humidity"], marker='^', linestyle='-', label="Humidity (%)")

    plt.title(f"Weather Data for {city.capitalize()}")
    plt.xlabel("Date & Time")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Отримати графік погоди для вказаного міста')
    parser.add_argument('city', type=str, help='Назва міста (наприклад: kyiv, london, tokyo)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
  
    plot_weather_data(args.city)

