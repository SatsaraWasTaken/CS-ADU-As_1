# Gets The Input
N = int(input("Enter a decimal to convert into binary: "))

result = ""  # Start with an empty string and fill up
M = N  # Creating a different variable so I can keep the initial number
while True:
    kalan = M % 2  # Find the remainder
    result = str(kalan) + result  # Create the binary form right to left
    M = M // 2
    if M == 0:  # Stop when the number is 0
        break

# Prints the result
print(f"{N} in binary is {result}")