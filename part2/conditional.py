number=int(input("Give me a number: "))

state = "even" if number % 2 == 0 else "odd"

print(f"The number {number} is {state}.")

a=10
b=20

greater = a if a > b  else b
print(f"{greater} is greater b/w {a} and {b}.")