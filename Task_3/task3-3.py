import random
print("Number guessing game")
guesses = 0
num = random.randint(1,100)
print("Guess a number between 1 and 100:")
while True :
    answer = int(input())
    guesses += 1
    if answer == num:
        print("Correct")
        print(f"It took you {guesses} guesses")
        break
    elif answer < num:
        print("Too low, try again:")
    elif answer > num:
        print("too high, try again:")