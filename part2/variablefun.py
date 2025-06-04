def add(*numbers): # you can pass any number of arguments, received as a tuple
    sum = 0
    for number in numbers:
        sum += number
    return sum

print("Sum of 1, 2, 3 is:", add(1, 2, 3))  # Example call with three arguments
print("Sum of 4, 5, 6, 7 is:", add(4, 5, 6, 7))  # Example call with four arguments\
print("Sum of 8, 9, 10, 11, 12 is:", add(8, 9, 10, 11, 12))
print ("Sum if no parameters Passed :", add ())  # Example call with no arguments, should return 0