import requests
import json
from datetime import datetime
from pathlib import Path


class MeteoAPI:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def fetch_and_save(self, output_dir: str):
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "current_weather": True,
            "hourly": "temperature_2m,precipitation,windspeed_10m"
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = Path(output_dir) / f"meteo_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Fichier météo créé : {filename}")


if __name__ == "__main__":
    meteo = MeteoAPI(latitude=48.8566, longitude=2.3522)
    meteo.fetch_and_save("../data/raw")
