##

import math

# Ask the user for a number
number = float(input("Please enter a number: "))

# Calculate the square root
square_root = math.sqrt(number)

# Calculate the natural logarithm
natural_log = math.log(number)

# Calculate the sine (in radians)
sine_value = math.sin(number)

# Display the results
print(f"\nResults for the number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm: {natural_log}")
print(f"Sine (in radians): {sine_value}")