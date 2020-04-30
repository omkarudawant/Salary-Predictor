# Import libraries
from numpy import array
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[array(data['exp'])]])

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(output)


if __name__ == '__main__':
	# Load the model
	model = joblib.load('../model/model.joblib')
	print(' * Model loaded successfully !!!')
	app.run(debug=False)