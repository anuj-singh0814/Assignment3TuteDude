#Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number (e.g., 5)
sample_number = 5
print(f"The factorial of {sample_number} is {factorial(sample_number)}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number (e.g., 5)
sample_number = 5
print(f"The factorial of {sample_number} is {factorial(sample_number)}")