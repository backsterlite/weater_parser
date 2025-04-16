import argparse
from weather import get_weather_data, save_weather_to_csv, plot_weather_data


def main():
    parser = argparse.ArgumentParser(description="WeatherWatcher CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: fetch
    fetch_parser = subparsers.add_parser("fetch", help="Fetch weather data for a city and save to CSV")
    fetch_parser.add_argument("city", type=str, help="City name (e.g., kyiv, london)")

    # Subcommand: plot
    plot_parser = subparsers.add_parser("plot", help="Plot weather data from CSV")
    plot_parser.add_argument("city", type=str, help="City name (e.g., kyiv, london)")

    args = parser.parse_args()

    if args.command == "fetch":
        data = get_weather_data(args.city)
        save_weather_to_csv(data, args.city)
        print(f"✅ Weather data for '{args.city}' saved.")

    elif args.command == "plot":
        plot_weather_data(args.city)


if __name__ == "__main__":
    main()