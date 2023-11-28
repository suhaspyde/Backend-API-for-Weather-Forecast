rom flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# API KEY
API_KEY = '1d36e5033d1ab26b49ac2324242bad74'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Weather data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
