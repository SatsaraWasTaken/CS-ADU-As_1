# The secret number user try to guess
secretNumber = 45
# I also added a counter
counter = 0

# A basic while loop
guess = int(input("Enter a number between 1-100: "))
while True :
    counter = counter + 1
    if secretNumber < guess :
        print("Too high! Try something smaller")
        guess = int(input("Enter a number between 1-100: "))
    elif secretNumber > guess :
        print("Too low! Try something bigger")
        guess = int(input("Enter a number between 1-100: "))
    else:
        print(f"You've guessed it in {counter} rounds! Well played.")
        break
