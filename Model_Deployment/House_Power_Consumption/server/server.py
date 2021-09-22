from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_col_names', methods=['GET'])
def get_col_names():
    response = jsonify({
        'columns': util.get_col_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_power_consumption', methods=['GET', 'POST'])
def predict_house_power_consumption():
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    temp_max = int(request.form['temp_max'])
    dew_max = int(request.form['dew_max'])

    response = jsonify({
        'expected_power_consumption': util.get_power_consumption(year,month,day,temp_max,dew_max)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for House Power Consumption..")
    util.load_saved_artifacts()
    app.run()