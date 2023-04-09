from random import choice, choices
from brain_games.major import major

rule = "What is the result of the expression?"

operator = choice(["+", "-", "*"])


def calculating(num_1, num_2, operator):
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    return result


def quest_func():
    num1, num2 = choices(range(1, 15), k=2)
    answer = calculating(num1, num2, operator)
    question = "{} {} {}".format(num1, operator, num2)
    return question, str(answer)


def run_game():
    major(quest_func, rule)
