from flask import Flask, render_template
from pip._internal.resolution.resolvelib import candidates

import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:id>")
def get_candidate(id):
    candidate = utils.get_candidate_by_pk(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skills(skill):
    candidates = utils.get_candidates_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


app.run(debug=True)
