import prompt

NUM_ATTEMPTS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.RULE)
    
    for i in range(NUM_ATTEMPTS):
        question, correct_answer = game.get_game()
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
