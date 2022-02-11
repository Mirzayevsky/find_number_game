import random


def my_action(defaultNumber=10):
    my_number = []
    input_number = input(f"I think number 1 from to {defaultNumber}. Can you find ? :  ")
    my_number.append(int(input_number))
    random_number = random.sample(range(1, defaultNumber), 1)

    def enter_input():
        new_value = input(">>>:  ")
        my_number.append(int(new_value))

    def delete_function(my_number):
        del my_number[0]

    def function_pick():
        return enter_input(), delete_function(my_number)

    def condition_function(x, y):
        guessing = 0

        mark_one = True
        while mark_one:
            guessing += 1

            if x[0] <= 0:
                print(" Wrong! Please entered number will be upper than number of 0! ")
                function_pick()

            elif x[0] > defaultNumber:
                print(f" Wrong! Please entered number will be lower than number of {defaultNumber}! ")
                function_pick()

            elif x < y:
                print("my number  upper  than your number. Try again:")
                function_pick()

            elif x > y:
                print("my number  lower  than your number. Try again:")
                function_pick()

            elif x == y:
                print(f"Congratulations ! you win with taxminlar {taxminlar} ")
                mark_one = False

        return guessing

    condition_function(my_number, random_number)


# my_action()


def number_pc(x=10):
    low = 1
    high = x
    input(f"Think 1 from to {x} and enter any number. I will find ")
    guessing = 0
    while True:
        guessing += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        answer = input(f"you think {guess}: (t),"f"my number upper than this (+),or lower".lower())
        if answer == "-":
            high = guess - 1
        elif answer == "+":
            low = guess + 1
        else:
            break
    print("found")
    return taxminlar


# number_pc()

def play(defaultNumber=10, x=10):

    again = True
    while again:
        guessing_user = my_action(defaultNumber)

        guessing_pc = number_pc(x)

        if guessing_user > guessing_pc:
            print("I win")
        elif guessing_user < guessing_pc:
            print("you win")
        else:
            print("equal")
            again = int(input("Do you want to pay again ? Yes(1),No(0): "))


play()
