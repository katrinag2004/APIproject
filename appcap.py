from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

capital_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Canberra": "Australia/Sydney",
    "New Delhi": "Asia/Kolkata"
    # Add more as needed
}


@app.route('/api/time', methods=['GET'])
def get_time():
    token = request.headers.get('Authorization')
    if not token or token != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized. Please provide a valid token."}), 401

    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a capital city using ?city="}), 400

    if city not in capital_timezones:
        return jsonify({"error": f"'{city}' is not in our database."}), 404

    tz_name = capital_timezones[city]
    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)
    offset = now.strftime('%z')
    offset_hours = f"{offset[:3]}:{offset[3:]}"

    return jsonify({
        "city": city,
        "current_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": offset_hours
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
