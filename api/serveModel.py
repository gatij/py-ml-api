from flask import Flask, jsonify, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Determine the correct path to the model file
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.joblib')

# Load the joblib model
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check if 'input' is in the request data
        if 'input' not in data:
            return jsonify({'error': 'Invalid input format: missing "input" key'}), 400

        # Prepare input data
        input_data = np.array(data['input']).reshape(1, -1)

        # Perform inference
        prediction = model.predict(input_data).tolist()

        # Convert prediction to human-readable form (optional)
        iris_species = ['setosa', 'versicolor', 'virginica']
        predicted_species = iris_species[prediction[0]]

        # Return the prediction as JSON response
        return jsonify({'prediction': predicted_species}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
