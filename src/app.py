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

        # This approach is NOT RECOMMENDED because of no separation of concerns, 
        # user interface for prediction and business logic for model are mixed in this file.
        # cf: Method2 in index.html
        # Method1: This method uses Pythonic code to display the prediction text.
        # This will Convert prediction to a human-readable format
        # If prediction is 0, display "Customer is likely to churn."
        # If prediction is 1, display "Customer is unlikely to churn."
        # If prediction is not defined, display "Click 'Predict' to generate Model Prediction!"
        # 
        if prediction == 0:
            prediction_text = "Customer is likely to churn."
        elif prediction == 1:
            prediction_text = "Customer is unlikely to churn."
        else:
            prediction_text = "Undefined!"
        # Render the template with prediction and input data
        return render_template('index.html', prediction=prediction, 
                               display=prediction_text, input=form_input)
    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    print(request_data)

    print(3/0)  # Intentional error for demonstration
    return {'success': False} # This will return a 500 error (Internal Server Error)
    # return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
