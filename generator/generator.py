from random import randint

from .nouns import NOUNS
from .adjectives import ADJECTIVES

def get_random_name():
    return _get_random_adjective() + " " + _get_random_noun()

def get_possible_combinations():
    noun_count = len(NOUNS)
    adjective_count = len(ADJECTIVES)
    possible_combinations = noun_count * adjective_count
    return possible_combinations

def get_nouns():
    return NOUNS

def get_adjectives():
    return ADJECTIVES

def _get_random_noun():
    return _get_random_word(NOUNS)

def _get_random_adjective():
    return _get_random_word(ADJECTIVES)

def _get_random_word(words):
    word_count = len(words)
    random_index = randint(0, word_count - 1)
    random_word = words[random_index]
    return random_word
