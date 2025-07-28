# Example Demo: Using Flask to Serve a Model Prediction via API
# This script serves an API endpoint that allows users to provide data via JSON requests and receive predictions via JSON response from a machine learning model.
# It uses Flask for the web framework and assumes a pre-trained model is available in the specified directory.

# This script is designed to be run in a Python environment with Flask installed.
# It provides a simple web interface for users to input their data, which is then processed by a machine learning model to generate predictions.
# It also includes dynamic error handling to ensure that user inputs are validated across requests.

# Sanity Check for Model Prediction (using model) via API
# Required1: Flask installed
# Required2: src/app-prediction-json-model-errhdlr.py in src directory
# Required3: src/templates/index.html in src/templates directory
# Required4: src/model.py in src directory
# Required5: model/catboost_model.pkl in model directory
# Required6: notebooks/api_query_prediction.ipynb in notebooks directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/app-prediction-json-model-errhdlr.py

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

    # Check if request_data is a list and has exactly 6 elements
    if len(request_data) != 6:
        return {'success': False, 'error': 'Input features must contain exactly 6 elements'}, 400
    
    required_keys = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    
    for key in required_keys:
        if key not in request_data:
            # return {'success': False, 'error': f'Missing required input data: {key}'}, 400
            return {'error': f'"{key}" not found in json.'}, 400
        
    # Check if request_data is empty
    if not request_data:
        return {'success': False, 'error': 'No input data provided'}, 400
    
    # Check if all required keys are present
    # if not all(key in request_data for key in required_keys):
    #     return {'success': False, 'error': 'Missing required input data'}, 400
    if any(key not in request_data for key in required_keys):
        return {'success': False, 'error': 'Missing required input data'}, 400
    
    # Check if the input data types are correct
    try:
        age = int(request_data['age'])  # Ensure age is an integer
        sex = request_data['sex']  # Ensure sex is a string
        bmi = float(request_data['bmi'])  # Ensure bmi is a float
        children = int(request_data['children'])  # Ensure children is an integer
        smoker = request_data['smoker']  # Ensure smoker is a string
        region = request_data['region']  # Ensure region is a string
    except (ValueError, TypeError) as e:
        return {'success': False, 'error': f'Invalid input data: {str(e)}'}, 400
    
    # Check if the input values are within expected ranges
    if age < 0 or bmi < 0 or children < 0:
        return {'success': False, 'error': 'Input values must be non-negative'}, 400
    if sex not in ['male', 'female']:
        return {'success': False, 'error': 'Invalid value'}, 400
    if smoker not in ['yes', 'no']:
        return {'success': False, 'error': 'Invalid value for smoker'}, 400
    if region not in ['northeast', 'northwest', 'southeast', 'southwest']:
        return {'success': False, 'error': 'Invalid value for region'}, 400
    
    # Check if the Model class is properly defined and can be instantiated
    if not hasattr(Model, '__init__'):
        return {'success': False, 'error': 'Model class is not defined properly'}, 500
    if not Model():
        return {'success': False, 'error': 'Model instantiation failed'}, 500
    
    # Check if the model file exists and can be loaded
    try:
        model_instance = Model()    # Instantiate the model
    except Exception as e:
        return {'success': False, 'error': f'Model loading failed: {str(e)}'}, 500
    
    # Check if the predict method exists and can be called
    if not hasattr(model_instance, 'predict'):
        return {'success': False, 'error': 'Model does not have a predict method'}, 500
    if not callable(model_instance.predict):
        return {'success': False, 'error': 'Model predict method is not callable'}, 500
    
    
    
    # If all checks pass, proceed with the prediction
    # Assuming Model class has a predict method that takes a list of inputs
    if not hasattr(Model, 'predict'):
        return {'success': False, 'error': 'Model class does not have a predict method'}, 500
    if not Model().predict:
        return {'success': False, 'error': 'Model prediction failed'}, 500
    
    # Modified code
    age = int(request_data['age'])
    sex = request_data['sex']
    bmi = float(request_data['bmi'])
    children = int(request_data['children'])
    smoker = request_data['smoker']
    region = request_data['region']

    model_inputs = [age, sex, bmi, children, smoker, region]

    # Check if the input features are in the correct format for prediction
    if not isinstance(model_inputs, list):
        return {'success': False, 'error': 'Input features must be a list'}, 400
    if len(model_inputs) != 6:
        return {'success': False, 'error': 'Input features must contain exactly 6 elements'}, 400
    if any(not isinstance(feature, (int, float, str)) for feature in model_inputs):
        return {'success': False, 'error': 'Input features must be of type int, float, or str'}, 400
    
    prediction = Model().predict(model_inputs)

    # Check if the model can make a prediction with the given input features
    try:
        prediction = model_instance.predict(model_inputs)   # Call the predict method with the input features
    except Exception as e:
        return {'success': False, 'error': f'Model prediction failed: {str(e)}'}, 500
    
    # Check if the prediction result is in the expected format
    if not isinstance(prediction, (int, float)):
        return {'success': False, 'error': 'Prediction result must be a numerical value'}, 500
    if prediction is None:
        return {'success': False, 'error': 'Prediction result is None'}, 500
    if not prediction:
        return {'success': False, 'error': 'Prediction result is empty'}, 500
    if isinstance(prediction, list) and len(prediction) == 1:
        prediction = prediction[0]
    if prediction < 0:
        return {'success': False, 'error': 'Prediction result must be non-negative'}, 500
    if prediction == 0:
        return {'success': False, 'error': 'Prediction result cannot be zero'}, 500
    
    return {'prediction': prediction}


if __name__ == '__main__':
    app.run(debug=True)
