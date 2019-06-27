from flask import Flask, jsonify, request
from main import main
app = Flask(__name__)


@app.route('/median_pickup_time', methods=['GET'])
def find_pickup_time():
    location = request.args.get('location_id', default=1, type=int)
    start_time = request.args.get('start_time', default='', type=str)
    end_time = request.args.get('end_time', default='', type=str)

    # Standardlize with data from csv
    start_time += "Z"
    end_time += "Z"

    result = main(location, start_time, end_time)
    return jsonify({'median': result})


if __name__ == '__main__':
    app.run(debug=True, port=8080)