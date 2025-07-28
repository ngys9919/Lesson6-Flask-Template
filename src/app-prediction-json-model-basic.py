# Example Demo: Using Flask to Serve a Model Prediction via API
# This script serves an API endpoint that allows users to provide data via JSON requests and receive predictions via JSON response from a machine learning model.
# It uses Flask for the web framework and assumes a pre-trained model is available in the specified directory.

# This script is designed to be run in a Python environment with Flask installed.
# It provides a simple web interface for users to input their data, which is then processed by a machine learning model to generate predictions.
# It excludes any error handling to ensure that user inputs are validated across requests.

# Sanity Check for Model Prediction (using model) via API
# Required1: Flask installed
# Required2: src/app-prediction-json-model-basic.py in src directory
# Required3: src/templates/index.html in src/templates directory
# Required4: src/model.py in src directory
# Required5: model/catboost_model.pkl in model directory
# Required6: notebooks/api_query_prediction.ipynb in notebooks directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/app-prediction-json-model-basic.py

# To test:
# 1. Run the Flask app using the command above.
# 2. Open the Jupyter Notebook at notebooks/api_query_prediction.ipynb.
# 3. Execute the cells in the notebook to send a POST request to the API endpoint.
# The prediction should be in JSON format based on the model predicted values as follows:

# <Response [200]>
# {
#   "prediction": 17353.51581464062
# }

from flask import Flask, request, render_template
from model import Model  # Assuming you have a model.py file with a Model class

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)
        # Modified code
        age = int(form_input['age'])
        sex = form_input['sex']
        bmi = float(form_input['bmi'])
        children = int(form_input['children'])
        smoker = form_input['smoker']
        region = form_input['region']

        model_inputs = [age, sex, bmi, children, smoker, region]
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction, input=form_input)
    return render_template('index.html')


# Method 2: Via POST API (JSON response for demonstration)
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)
    
    # Modified code
    age = int(request_data['age'])
    sex = request_data['sex']
    bmi = float(request_data['bmi'])
    children = int(request_data['children'])
    smoker = request_data['smoker']
    region = request_data['region']

    model_inputs = [age, sex, bmi, children, smoker, region]
    prediction = Model().predict(model_inputs)

    # Return the prediction as a JSON response
    return {'prediction': prediction}


if __name__ == '__main__':
    app.run(debug=True)
