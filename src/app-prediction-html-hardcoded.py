# Example Demo: 
# Sanity Check for Model Prediction (using hardcoded) via HTML
# Required1: Flask installed
# Required2: src/app-prediction-html-hardcoded.py in src directory
# Required3: src/templates/index.html in src/templates directory
# Required4: src/model.py in src directory
# Required5: model/catboost_model.pkl in model directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/app-prediction-html-hardcoded.py

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
# The prediction should be a numerical value based on the hardcoded input values.

from flask import Flask, request, render_template

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)
        prediction = 1234  # Hardcoded prediction for demonstration purposes
        # In a real application, you would use the Model class to make a prediction
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
