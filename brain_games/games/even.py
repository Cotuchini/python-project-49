from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    question = randint(0, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
