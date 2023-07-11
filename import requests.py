import requests
import time
import matplotlib.pyplot as plt

api_url = "http://api.open-notify.org/iss-now.json"
data_points = 100
duration_interval = 10

def tracker():
    latitudes, longitudes, timestamps = [], [], []

    for _ in range(data_points):
        response = requests.get(api_url)
        data = response.json()

        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        timestamp = int(data["timestamp"])

        latitudes.append(latitude)
        longitudes.append(longitude)
        timestamps.append(timestamp)

        time.sleep(duration_interval)

    return latitudes, longitudes, timestamps


def plotter(latitudes, longitudes):
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, latitudes, "b.-")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("International Space Station Path")
    plt.grid(True)
    plt.show()


def main():
    latitudes, longitudes, _ = tracker()
    plotter(latitudes, longitudes)


main()