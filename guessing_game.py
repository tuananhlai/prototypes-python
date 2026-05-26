from random import randint

lo = 1
hi = 100
answer = randint(lo, hi)
numAttempts = 0

print(f"I'm thinking of a number between {lo} and {hi}.")
while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("That's not a number.")
        continue

    numAttempts += 1

    if guess == answer:
        break
    elif guess < answer:
        print("Higher")
    else:
        print("Lower")

print(
    f"The answer is {answer}! You guessed correctly in {numAttempts} attempt(s).")
