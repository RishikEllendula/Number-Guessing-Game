import random

lower = 0
upper = 1000
max_attempts = 5
secret = random.randint(lower, upper)

def guess():
    while True:
        try:
            n = int(input(f"Enter a number between {lower} and {upper}: "))
            print(f"DEBUG: You entered {n}")
            if lower <= n <= upper:
                return n
            else:
                print("Invalid input")
        except ValueError:
            print("Entered value is not a number")

def check(n, secret):
    if n == secret:
        return "Correct"
    elif n < secret:
        return "Too bad, it's a bit low"
    else:
        return "Too bad, it's a bit high"

def game():
    attempts = 0
    while attempts < max_attempts:
        g = guess()
        c = check(g, secret)
        if c == "Correct":
            print(f"Wow Hurray!!! 🥳🥳 Congratulations, your answer was correct.")
            print(f"Number of attempts left: {max_attempts - attempts - 1}")
            break
        else:
            print(c)
        attempts += 1
    else:
        print("Oww, you completed your attempts.. HAHAHA😁😂")
        print(f"Secret number was {secret}")

game()