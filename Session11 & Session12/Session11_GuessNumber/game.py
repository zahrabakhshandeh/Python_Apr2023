# 1 - 100 ===> 
# user < number
# user > number
# user == number ===> end
import random
from func import user_input

print("I'm thinking a number between 1 and 100")
number = random.randint(1, 100)
print(number)
c = 0
while True:
    user_guess = user_input("Enter your guess: ")
    c += 1
    try:
        if user_guess < 1 or user_guess > 100:
            raise ValueError("number between 1 and 100")
    except ValueError:
        print("error")
        continue
    """if user_guess < 1 or user_guess > 100:
        print("number between 1 and 100")"""
    if user_guess == number:
        print(f"you gussed the number. ({c})")
        break
    elif user_guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")