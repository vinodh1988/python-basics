number = int(input("Enter a number: "))

if number % 5 == 0 and number % 7 == 0 and number % 11 == 0:
    print(f"{number} is divisible by 5, 7, and 11.")
else:
    print(f"{number} is not divisible by 5, 7, and 11.")