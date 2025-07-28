# Example Demo: 
# Sanity Check for Model Prediction (using hardcoded) via API
# Required1: Flask installed
# Required2: src/app-prediction-json-hardcoded.py in src directory
# Required3: src/templates/index.html in src/templates directory
# Required4: src/model.py in src directory
# Required5: model/catboost_model.pkl in model directory
# Required6: notebooks/api_query_example.ipynb in notebooks directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/app-prediction-json-hardcoded.py

# To test:
# 1. Run the Flask app using the command above.
# 2. Open the Jupyter Notebook at notebooks/api_query_example.ipynb.
# 3. Execute the cells in the notebook to send a POST request to the API endpoint.
# The prediction response should be hardcoded as the following in JSON format:

# <Response [500]>
# {
#   "success": false
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


# Method 2: Via POST API (hardcoded JSON response for demonstration)
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
