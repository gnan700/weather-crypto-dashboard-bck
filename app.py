from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React

WEATHER_API_KEY = "f151cf71d55af767fa3bc4513b0b6b73"
NEWS_API_KEY = "966708bf382b42aeb51a05be349aa454"
CRYPTO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

cities = ["Bengaluru", "Mumbai", "Chennai"]

# Fetch weather data
@app.route("/weather", methods=["GET"])
def get_weather():
    weather_data = []
    for city in cities:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        weather_data.append(response.json())
    return jsonify(weather_data)

# Fetch cryptocurrency prices
@app.route("/crypto", methods=["GET"])
def get_crypto():
    response = requests.get(
        f"{CRYPTO_API_URL}?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd"
    )
    return jsonify(response.json())

# Fetch top 5 news headlines
@app.route("/crypto-news", methods=["GET"])
def get_crypto_news():
    url = f"https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get("articles", [])[:5]  # Get only first 5 articles
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
