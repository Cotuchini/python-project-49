from random import randint
from brain_games.major import major

rule = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

def quest_func():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer  

def run_game():
    major(quest_func, rule)
