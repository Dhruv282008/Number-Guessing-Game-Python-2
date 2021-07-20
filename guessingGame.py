name = input("What is your name?: ")

print("Hi",name,"Let's play a Number Guessing Game")

print("Hint : { The number is a 5 digit number and lies between 10000 - 15000 is a rounded off number.{10000 or 13000 or 15000}}, You will get only 1 chance to play this game")

uinput = input("Enter the Number : ")

numbers = [10000, 13000, 15000]

import random
randchoice = random.choice(numbers)

if uinput == randchoice:
    print("You won!, You have given the correct answer")

if uinput != randchoice:
    print("Wrong Answer. The number was", randchoice)    
