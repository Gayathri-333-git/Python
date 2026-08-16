import random
guess = int(input("Enter a number: "))
number = random.randint(1, 10)
if guess == number:
    print("Correct")
elif guess >= number:
    print("Too high")
else:
    print("Too low")
