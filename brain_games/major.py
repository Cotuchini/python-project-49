import prompt

num_attempts = 3


def major(quest_func, rule):
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(user_name))
    print(rule)
    for i in range(num_attempts):
        question, correct_answer = quest_func()
        print("Question: {}".format(question))
        user_answer = prompt.string("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, correct_answer
                )
            )
            print("Let's try again, {}!".format(user_name))
            return
    print("Congratulations, {}!".format(user_name))
