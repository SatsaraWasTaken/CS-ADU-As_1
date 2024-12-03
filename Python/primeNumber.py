# Gets input
N = int(input("Enter a number: "))

if N < 2:
    print("There are no prime numbers in the area")
else:
    for num in range(2, N + 1):  # Check numbers from 2 to N
        isPrime = True  # Assume all numbers are prime
        for i in range(2, int(num ** 0.5) + 1):  # Check divisors from 2 to sqrt(num)
            if num % i == 0:  # If divisible, it's not a prime and we go back to get a new number
                isPrime = False
                break  # No need to check further
        if isPrime:  # If the number is still considered prime
            print(num, end=" ")  # Print the prime number on the same line
