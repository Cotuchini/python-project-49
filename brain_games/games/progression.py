
from random import choice, randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    length = 10
    maximum_number = (delta * length) + initial_number
    return range(initial_number, maximum_number, delta)


def get_game():
    prog = generate_progression()
    secret = choice(prog)
    progression = ' '.join([
        '..' if num == secret else str(num) for num in prog
    ])
    question = f'Question: {progression}'
    return (question, str(secret))
