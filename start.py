from flask import Flask
from random import randint
import data.nouns as Nouns
import data.adjectives as Adjectives


app = Flask(__name__)

@app.route("/")
def index():
    return get_random_name()

def get_random_name():
    return get_random_adjective() + " " + get_random_noun()

def get_random_noun():
    return get_random_word(Nouns.nouns)

def get_random_adjective():
    return get_random_word(Adjectives.adjectives)

def get_random_word(words):
    word_count = len(words)
    random_index = randint(0, word_count - 1)
    random_word = words[random_index]
    return random_word

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
