import json

from flask import render_template

from app import app
from generator import generator

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/random_name")
def random_name():
    random_name = generator.get_random_name()
    nameObj = {
        "name": random_name
    }
    result = json.dumps(nameObj)
    return result

@app.route("/possible_combinations")
def possible_combinations():
    possible_combinations = generator.get_possible_combinations()
    pcObj = {
        "possible_combinations": possible_combinations
    }
    result = json.dumps(pcObj)
    return result

@app.route("/nouns")
def nouns():
    nouns = generator.get_nouns()
    nounsObj = {
        "nouns": nouns
    }
    result = json.dumps(nounsObj)
    return result

@app.route("/adjectives")
def adjectives():
    adjectives = generator.get_adjectives()
    adjectivesObj = {
        "adjectives": adjectives
    }
    result = json.dumps(adjectivesObj)
    return result
