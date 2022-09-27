from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH SEEKRIT"

@app.route('/')
def load_home():
    session['satisfaction'] = []
    return render_template("home.html")


@app.route('/satisfaction_survey', methods=["GET"])
def load_survey():
    answer = request.args
    counter = 0
    if answer:
        session['satisfaction'].append(answer)
        counter = len(session['satisfaction'])
        # import pdb
        # pdb.set_trace()
    survey = surveys.satisfaction_survey
    questions = survey.questions
    render_template("survey.html")
    if len(session['satisfaction']) < len(questions):
        return render_template("question.html", question=questions[counter])
    return render_template("thanks.html")
