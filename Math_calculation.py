from art import *
import random

OPERATORS = ["*", "+", "-"]


MIN_OPERAND = 1
MAX_OPERAND = 10
TOTAL_PROBLEMS = 20

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expr = str(left) + " " + operators + " " + str(right)
    answer = eval(expr)
    if answer >= 0:
        return expr, answer
    return generate_problem()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Задача № " + str(i + 1) + ': ' + expr + " = ")
        if guess == str(answer):
            break
tprint("You Win!", font="xlarge")


