def maxOdd(numbers):
    """
    Returns the maximum odd number from a list of integers.
    If no odd number is found, returns None.
    """
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return max(odd_numbers) if odd_numbers else None

def maxEven(numbers):
    """
    Returns the maximum even number from a list of integers.
    If no even number is found, returns None.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    return max(even_numbers) if even_numbers else None