names=['Rebecca', 'John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve','Siddharth', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack', 'Kathy', 'Liam', 'Mia', 'Nina', 'Oscar', 'Paul']
try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    c=a/b
    print(f"The result of {a} divided by {b} is {c}")
    index=int(input("Enter an index to access the names list: "))
    print(f"The name at index {index} is {names[index]}")
except ZeroDivisionError as e:
    print(f"Error: Cannot divide by zero. {e}")
except IndexError as e:
    print(f"Error: Index {index} is out of range for the names list. {e}")
except ValueError as e:
    print(f"Error: Invalid input. Please enter a valid number. {e}")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No exceptions occurred. Everything executed successfully.")
finally:
    print("Execution completed. Thank you for using the program.")