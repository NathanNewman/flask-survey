from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

response = []
if session["satisfaction"]:
    responses = session["satisfaction"]


@app.route('/')
def load_home():
    return render_template("home.html")


@app.route('/satisfaction_survey', methods=["GET"])
def load_survey():
    answer = request.args
    counter = len(responses) - 1
    if answer:
        responses.append(answer)
        session["satisfaction"] = responses
    survey = surveys.satisfaction_survey
    questions = survey.questions
    render_template("survey.html")
    if len(responses) < len(questions):
        return render_template("question.html", question=questions[counter])
    return render_template("thanks.html")
