# Demonstration of the range() function in Python
print(range(5))
print(list(range(5)))  # Convert to list for better visualization
print(list(range(1, 10)))  # Range from 1 to 9


# Basic usage: range(stop)
print("range(5):", list(range(5)))  # [0, 1, 2, 3, 4]

# range(start, stop)
print("range(2, 7):", list(range(2, 7)))  # [2, 3, 4, 5, 6]

# range(start, stop, step)
print("range(1, 10, 2):", list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# range with negative step
print("range(10, 0, -2):", list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]

print(list(range(5, -6, -1)))  # [5, 3, 1]

# Using range in a for loop
