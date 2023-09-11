from art import *
import random


class MY_class():

    def __init__(self):

        self.TOTAL_PROBLEMS = 5

    def generate_problem(self):
        big_fruit = random.choice(["Ябълка", "Тиква", "Круша"])
        a = random.randint(1, 1)
        medium_fruit = random.choice(["Мандарини", "Картофа", "Портокала"])
        b = random.randint(2, 10)
        small_fruit = random.choice(["Боровинки", "Ягоди", "Череши"])
        c = random.randint(2, 10)

        expr = f"1 {big_fruit} тежи колкото {b} {medium_fruit}. 1 {medium_fruit} тежи колкото {c} {small_fruit}." \
               f" Колко {small_fruit} тежът колкото една {big_fruit}"
        real_answer = (b*c)
        answer = eval(str(real_answer))
        return expr, answer


    def Range(self):
        for i in range(self.TOTAL_PROBLEMS):
            expr, answer = self.generate_problem()
            while True:
                guess = input("Задача № " + str(i + 1) + ': ' + expr + " = ")
                if guess == str(answer):
                    break


My_object = MY_class()
My_object.generate_problem()
My_object.Range()

tprint("You Win!", font="xlarge")


