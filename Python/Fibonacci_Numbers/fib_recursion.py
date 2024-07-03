# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Get number of iterations from the user
num_iterations = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci(num_iterations)

# Print the result
print(f"The first {num_iterations} Fibonacci numbers are: {fib_sequence}")

