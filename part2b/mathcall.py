import mymath
from mymath import sum, factorial, oddproduct

print(mymath.sum(5, 10))  # Output: 15
print(mymath.sum(5, 10, 15))  # Output: 30
print("factorial(5)", mymath.factorial(5))  # Output: 120
print("multiply(5, 10)", mymath.oddproduct(5, 10))  # Output: 50
print("multiply(5, 10, 15)", mymath.oddproduct(5, 10, 15))  # Output: 750
print(sum(5, 10))  # Output: 15