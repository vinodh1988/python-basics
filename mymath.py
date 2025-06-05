def sum(*numbers):
    """Returns the sum of any number of arguments."""
    total = 0
    for number in numbers:
        total += number
    return total

def oddproduct(*numbers):
    """Returns the product of odd numbers from the given arguments."""
    product = 1
    for number in numbers:
        if number % 2 != 0:  # Check if the number is odd
            product *= number
    return product if product != 1 else 0  # Return 0 if no odd numbers are found

def evenproduct(*numbers):
    """Returns the product of even numbers from the given arguments."""
    product = 1
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            product *= number
    return product if product != 1 else 0  # Return 0 if no even numbers are found

def factorial(n):
    """Returns the factorial of a given number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result