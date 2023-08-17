from flask import Flask, render_template, request
from notion_api import add_participant_row
from openai_api import create_workout

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Survey Website!'

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Process form submission and save survey data
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        sex = request.form['sex']
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        response = add_participant_row(name, date_of_birth, sex, height, weight)

        workout = create_workout(name, date_of_birth, sex, height, weight)


        return workout
    else:
        # Render the survey form template
        return render_template('survey_form.html')