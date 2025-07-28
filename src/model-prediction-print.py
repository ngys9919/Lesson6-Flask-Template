import joblib


class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)

# Example Demo: 
# Sanity Check for Model Class
# Required1: model/catboost_model.pkl in model directory
# Required2: src/model-prediction-print.py in src directory

# To run:
# (venv) 
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/model-prediction-print.py

beneficiary_example = {
    "age": 30,
    "sex": "female",
    "bmi": 20,
    "children": 1,
    "smoker": "yes",
    "region": "southwest"
}

# model_inputs -> X -> features (age, sex, bmi, children, smoker, region)
# list(beneficiary_example.values()) -> convert dict values to list
model_inputs = list(beneficiary_example.values())
print(model_inputs)                  # [30, 'female', 20, 1, 'yes', 'southwest']

# Model() -> load model -> catboost_model.pkl
# Model().predict(model_inputs) -> y -> target (charges) -> prediction
print(Model().predict(model_inputs)) # 17353.51581464062

# (venv) 
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/model-prediction-print.py
# [30, 'female', 20, 1, 'yes', 'southwest']
# 17353.51581464062