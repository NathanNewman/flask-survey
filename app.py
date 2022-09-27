from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"


@app.route('/')
def load_home():
    session['satisfaction'] = []
    session['personality'] = []
    return render_template("home.html")


@app.route('/satisfaction_survey', methods=["GET"])
def load_survey():
    responses = session['satisfaction']
    session['satisfaction'] = responses
    answer = request.args
    counter = 0
    if answer:
        responses.append(answer)
        counter = len(responses)
    survey = surveys.satisfaction_survey
    questions = survey.questions
    render_template("survey.html")
    if len(session['satisfaction']) < len(questions):
        return render_template("question.html", question=questions[counter])
    return render_template("thanks.html")


@app.route('/personality_quiz', methods=["GET"])
def load_quiz():
    responses = session['personality']
    session['personality'] = responses
    answer = request.args
    counter = 0
    if answer:
        responses.append(answer)
        counter = len(responses)
        # import pdb
        # pdb.set_trace()
    survey = surveys.personality_quiz
    questions = survey.questions
    render_template("survey.html")
    if len(session['personality']) < len(questions):
        return render_template("question.html", question=questions[counter])
    return render_template("thanks.html")
