from flask import Flask, render_template, request

app = Flask(__name__)

app.debug = True

@app.route('/')
def home():
    return 'Welcome to the Survey Website!'

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Process form submission and save survey data
        return 'Thank you for taking the survey!'
    else:
        # Render the survey form template
        return render_template('survey_form.html')