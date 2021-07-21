# stone,paper,scissor

import random

lst = ['stone', 'paper', 'scissor']

chance = 7
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t stone,paper,scissor Game\n \n")
print("stone \npaper \nscissor \n")
print("you have only 7 chances")

# making the game in while
while no_of_chance < chance:
    _input = input('stone,paper,scissor:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter stone
    elif _input == "stone" and _random == "paper":
        computer_point = computer_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "stone" and _random == "scissor":
        human_point = human_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter paper
    elif _input == "paper" and _random == "scissor":
        computer_point = computer_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "paper" and _random == "stone":
        human_point = human_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter scissor

    elif _input == "scissor" and _random == "paper":
        human_point = human_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "scissor" and _random == "stone":
        computer_point = computer_point + 1
        print(f"you choose {_input} and computer choose {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# stone,paper,scissor Game in Python
# the stone breaks the scissor , the paper catch the stone , the scissor cuts the paper
#


