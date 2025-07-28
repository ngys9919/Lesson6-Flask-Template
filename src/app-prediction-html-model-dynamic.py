# Example Demo: Using Flask to Serve a Model Prediction via HTML
# This script serves a web application that allows users to input data and receive predictions from a machine learning model.
# It uses Flask for the web framework and assumes a pre-trained model is available in the specified directory.

# This script is designed to be run in a Python environment with Flask installed.
# It provides a simple web interface for users to input their data, which is then processed by a machine learning model to generate predictions.
# It also includes dynamic data handling to ensure that user inputs are retained across requests.

# Sanity Check for Model Prediction (using model) via HTML
# Required1: Flask installed
# Required2: src/app-prediction-html-model-dynamic.py in src directory
# Required3: src/templates/index.html in src/templates directory
# Required4: src/model.py in src directory
# Required5: model/catboost_model.pkl in model directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/app-prediction-html-model-dynamic.py

# To test:
# 1. Open a web browser and go to http://localhost:5000
# 2. You should see the input form.
# 3. Fill in the form with the following values:
#    - Age: 30 
#    - Sex: Female
#    - BMI: 20 
#    - Children: 1
#    - Smoker: Yes
#    - Region: Southwest
# 4. Click the "Predict" button.
# 5. You should see the prediction result displayed on the same page.
# The prediction should be a numerical value based on the model predicted values.

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


# Method 2: Via POST API (hardcoded JSON response for demonstration)
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
