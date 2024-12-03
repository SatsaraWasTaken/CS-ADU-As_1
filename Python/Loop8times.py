
# counter
N = 0

# a for loop to get 8 variables
for i in range(8):
    sayi = int(input("Enter a number: "))
    if sayi % 2 == 0 and sayi % 7 == 0: # Checks the condition
        N = N + 1

# Prints the amount
print(f"There are {N} numbers that is both even and divisible by 7 based on your input.")