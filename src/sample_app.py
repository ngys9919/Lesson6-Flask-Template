# Example Demo: 
# Sanity Check for Flask Responses
# Required1: Flask installed
# Required2: src/sample_app.py in src directory

# To run:
# (venv)
# ERIC NG@LAPTOP-MT5ND6S9 MINGW64 ~/ha-ai300/Lesson6/Lesson6-Flask-Template (main)
# $ python src/sample_app.py

# To test:

# Test 1: Response with Text
# 1. Open a web browser and go to http://localhost:5000
# 2. You should see a welcome message.

# Test 2: Response with HTML template
# 1. Open a web browser and go to http://localhost:5000/html
# 2. You should see the content of index.html.

# Test 3: Response with JSON
# 1. Open a web browser and go to http://localhost:5000/json
# 2. You should see a JSON response: {"success": true}.

# Test 4: Response with File (Bonus)
# 1. Open a web browser and go to http://localhost:5000/file
# 2. You should see the download of the file catboost_model.pkl as filename your_model_file.pkl.


from flask import Flask, render_template, send_file

app = Flask(__name__)

# 1: Response with Text
@app.route('/')  # default method=['GET']
def home_page():
    return 'Welcome to the home page!'

# 2: Response with HTML template
@app.route('/html')
def get_html():
    return render_template('index.html')

# 3: Response with JSON
@app.route('/json')
def get_json():
    return {'success': True}

# 4: Response with File (Bonus)
@app.route('/file')
def get_file():
    file_path = '../model/catboost_model.pkl'
    return send_file(file_path, download_name='your_model_file.pkl',
                     as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
    