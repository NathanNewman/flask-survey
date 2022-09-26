from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

@app.route('/')
def load_home():
    return render_template("home.html")

@app.route('/satisfaction_survey')
def load_survey():
    survey = surveys.satisfaction_survey
    questions = survey.questions
    import pdb
    pdb.set_trace()
    return render_template("survey.html", questions=questions)
