from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

responses = []
counter = -1


@app.route('/')
def load_home():
    return render_template("home.html")


@app.route('/satisfaction_survey', methods=["GET"])
def load_survey():
    answers = request.args
    if answers:
        global counter
        counter += 1
        responses.append(answers)
    survey = surveys.satisfaction_survey
    questions = survey.questions
    render_template("survey.html")
    if len(responses) < len(questions):
        return render_template("question.html", question=questions[counter])
    return render_template("thanks.html")
