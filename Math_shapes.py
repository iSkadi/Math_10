import random

from art import tprint


class Shapes:
    TOTAL_PROBLEMS = 10
    shapes = ["square", "rectangle", "triangle", "square1", "rectangle1",
              "triangle1", "rectangle2", "rectangle3", "triangle2", "triangle3"]

    def generate_problem(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)


        shape = random.choice(self.shapes)
        expr = ""
        answer = ""
        if shape == "rectangle":
            expr = f"На колко е равна обиколката на правоъгълник със страни а = {a} см и b = {b} см?"

            real_answer = str((a + b) * 2)
            answer = eval(real_answer)
        elif shape == "rectangle1":
            d = str((a + b) * 2)
            expr = f"Обиколката на правоъгълник е {d} см. Едната му страна е {a} см. Колко сантиметра е дълга другата му страна? "
            real_answer = str(b)
            answer = eval(real_answer)
        elif shape == "rectangle2":
            d = str((a + (a+b)) * 2)
            expr = f"На колко е равна обиколката на правоъгълник със страни а = {a} см и b, която е с {b} см по дълга? "
            real_answer = str(d)
            answer = eval(real_answer)
        elif shape == "rectangle3":
            d = str((a + (2*a)) * 2)
            expr = f"На колко е равна обиколката на правоъгълник със страни а = {a} см и b, която два пъти по дълга? "
            real_answer = str(d)
            answer = eval(real_answer)

        elif shape == "square":
            expr = f"На колко е равна обиколката на квадрат със страна а = {a} см? "
            real_answer = str((a * 4))
            answer = eval(real_answer)
        elif shape == "square1":
            d = str((a * 4))
            expr = f"Обиколката на квадрат е {d} см. Колко сантиметра е дълга страна му? "
            real_answer = str(a)
            answer = eval(real_answer)
        elif shape == "triangle":
            expr = f"На колко е равна обиколката на триъгълник със страни а = {a} см, b = {b} см и c = {c} см?"
            real_answer = str((a + b + c))
            answer = eval(real_answer)
        elif shape == "triangle1":
            d = str((a + b + c))
            expr = f"Обиколката на триъгълник е {d} см. Едната му страна е {a} см, другата {b} см. Колко сантиметра е дълга третата му страна? "
            real_answer = str(c)
            answer = eval(real_answer)
        elif shape == "triangle2":
            d = str(((2*a) + c))
            expr = f"На колко е равна обиколката на равнобедрен триъгълник със бедра(катети) = {a} см и основа = {c} см?"
            real_answer = str(d)
            answer = eval(real_answer)
        elif shape == "triangle3":
            d = str((3*a))
            expr = f"На колко е равна обиколката на равностранен триъгълник (има 3 равни страни), ако едната му страна е равна на {a} см?"
            real_answer = str(d)
            answer = eval(real_answer)

        return expr, answer

    def Range(self):
        for i in range(self.TOTAL_PROBLEMS):
            expr, answer = self.generate_problem()
            while True:
                guess = input("Задача № " + str(i + 1) + ': ' + expr + "  Отговор: ")
                if guess == str(answer):
                    break
                else:
                    not_correct = ["Try again", "You are wrong", "Wrong answer"]
                    tprint(random.choice(not_correct), "random")


My_object = Shapes()
My_object.generate_problem()
My_object.Range()

