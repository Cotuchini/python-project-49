from random import randint
from brain_games.major import major

rule = "What number is missing in the progression?"


def progress():
  start_num = randint(0, 80)
  step = randint(1, 20)
  sequence = []
  for i in range(10):
    sequence.append(start_num+i*step)
  return sequence


def quest_func():
    miss_item_index = randint(1, 10)
    order = progress()
    answer = order.pop(miss_item_index)
    order.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in order])
    return question, str(answer)


def run_game():
    major(quest_func, rule)
