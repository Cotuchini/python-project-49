from random import choices
from brain_games.major import major

rule = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    divider = min_num
    while divider > 0:
        if max_num % divider == 0 and min_num % divider == 0:
            return divider
        divider -= 1


def quest_func():
    num1, num2 = choices(range(1, 30), k=2)
    question = f'Question: {num1} {num2}'
    answer = get_gcd(num1, num2)
    return question, str(answer)


def run_game():
    major(quest_func, rule)
