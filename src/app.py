from flask import Flask, request, render_template

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        print(form_input)

    return render_template('index.html')


# Method 2: Via POST API
@app.route('/api/predict_one', methods=['POST'])
def predict_one():
    request_data = request.get_json()
    print(request_data)

    return {'success': False}, 500


if __name__ == '__main__':
    app.run(debug=True)
