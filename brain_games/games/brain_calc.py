import random

from brain_games.engine import check_answer, ask_user


def main():
    is_calc_correct()


def is_calc_correct():
    """Create randon +, _ or * with 2 numbers and check answer"""
    actions = ['+', '-', '*']
    first_num = random.randint(1, 14)
    second_num = random.randint(1, 14)
    random_action = random.choice(actions)
    math_question = f'{first_num} {random_action} {second_num}'
    print(f'What is {math_question}?')
    correct_answer = eval(math_question)
    checked_answer = check_answer(correct_answer, ask_user('integer'))
    print('Correct answer -', correct_answer)
    return checked_answer