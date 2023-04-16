from random import choice, choices

RULE = "What is the result of the expression?"

OPERATOR = choice(["+", "-", "*"])


def calculate_expression(random_num_1, random_num_2, OPERATOR):
    if OPERATOR == "+":
        result = random_num_1 + random_num_2
    elif OPERATOR == "-":
        result = random_num_1 - random_num_2
    elif OPERATOR == "*":
        result = random_num_1 * random_num_2
    return result


def get_game():
    random_num1, random_num2 = choices(range(1, 15), k=2)
    correct_answer = calculate_expression(random_num1, random_num2, OPERATOR)
    question = "{} {} {}".format(random_num1, OPERATOR, random_num2)
    return question, str(correct_answer)
