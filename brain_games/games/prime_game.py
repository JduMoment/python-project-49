from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

SMALLEST_NUMBER = 0
BIGGEST_NUMBER = 100


def is_prime(num):
    i = 2
    while num > i:
        is_prime = num % i
        i += 1
        if is_prime == 0:
            return False
    return True


def generate_question_and_answer():
    random_num = randint(SMALLEST_NUMBER, BIGGEST_NUMBER)
    correct_answer = "yes" if is_prime(random_num) else "no"
    question = f"{random_num}"
    return question, correct_answer
