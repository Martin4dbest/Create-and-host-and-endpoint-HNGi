from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get the  current UTC time
    utc_time = datetime.datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define GitHub URLs
    github_file_url = "https://github.com/Martin4dbest/Create-and-host-and-endpoint-HNGi/blob/main/app.py"
    github_repo_url = "https://github.com/Martin4dbest/Create-and-host-and-endpoint-HNGi"

    # Prepare the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
