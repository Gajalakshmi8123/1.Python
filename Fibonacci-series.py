a = 0
b = 1
num = int(input("Enter the limit for the Fibonacci sequence: "))

print("Fibonacci sequence:")
while a <= num:
    print(a, end=" ")  # Print the current Fibonacci number
    c = a + b  # Calculate the next Fibonacci number
    a = b  # Update `a` to the previous `b`
    b = c  # Update `b` to the newly calculated Fibonacci number
