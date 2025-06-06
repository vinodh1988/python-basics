## Python 

python is an interpreted language.

Python does not require variable declaration with explicit datatypes.

Although Python is dynamically typed, you can verify the type of data using the `type()` function.

The basic scalar data types supported in Python are:

* int
* float
* string
* bool

---

## Operators in Python

Python supports various operators for performing operations on variables and values. Each operator type is described below with its own table and notes.

### Arithmetic Operators

| Operator | Description                       | Example      | Result      |
|----------|-----------------------------------|-------------|-------------|
| `+`      | Addition                          | `a + b`     | Sum         |
| `-`      | Subtraction                       | `a - b`     | Difference  |
| `*`      | Multiplication                    | `a * b`     | Product     |
| `/`      | Division (float result)           | `a / b`     | Quotient    |
| `//`     | Floor Division (integer result)   | `a // b`    | Quotient    |
| `%`      | Modulus (remainder)               | `a % b`     | Remainder   |
| `**`     | Exponentiation                    | `a ** b`    | Power       |

**Notes:**
- Arithmetic operators work with numbers (`int`, `float`).
- `/` always returns a float, even if operands are integers.
- `//` returns the floor value of the division.

---

### Assignment Operators

| Operator | Description                        | Example      | Equivalent To   |
|----------|------------------------------------|--------------|-----------------|
| `=`      | Assign value                       | `a = 5`      |                 |
| `+=`     | Add and assign                     | `a += 2`     | `a = a + 2`     |
| `-=`     | Subtract and assign                | `a -= 2`     | `a = a - 2`     |
| `*=`     | Multiply and assign                | `a *= 2`     | `a = a * 2`     |
| `/=`     | Divide and assign                  | `a /= 2`     | `a = a / 2`     |
| `//=`    | Floor divide and assign            | `a //= 2`    | `a = a // 2`    |
| `%=`     | Modulus and assign                 | `a %= 2`     | `a = a % 2`     |
| `**=`    | Exponentiate and assign            | `a **= 2`    | `a = a ** 2`    |

**Notes:**
- Assignment operators combine assignment with arithmetic or bitwise operations.
- Useful for updating variable values concisely.

---

### Comparison Operators

| Operator | Description                | Example      | Result         |
|----------|----------------------------|--------------|----------------|
| `==`     | Equal to                   | `a == b`     | `True`/`False` |
| `!=`     | Not equal to               | `a != b`     | `True`/`False` |
| `>`      | Greater than               | `a > b`      | `True`/`False` |
| `<`      | Less than                  | `a < b`      | `True`/`False` |
| `>=`     | Greater than or equal to   | `a >= b`     | `True`/`False` |
| `<=`     | Less than or equal to      | `a <= b`     | `True`/`False` |

**Notes:**
- Used in conditional statements and loops.
- Always return a boolean value.

---

### Logical Operators

| Operator | Description        | Example           | Result         |
|----------|--------------------|-------------------|----------------|
| `and`    | Logical AND        | `a and b`         | `True`/`False` |
| `or`     | Logical OR         | `a or b`          | `True`/`False` |
| `not`    | Logical NOT        | `not a`           | `True`/`False` |

**Notes:**
- Used to combine multiple conditions.
- Evaluate to boolean values.

---

### Bitwise Operators

| Operator | Description              | Example      | Result         |
|----------|--------------------------|--------------|----------------|
| `&`      | Bitwise AND              | `a & b`      | Bitwise result |
| `|`      | Bitwise OR               | `a | b`      | Bitwise result |
| `^`      | Bitwise XOR              | `a ^ b`      | Bitwise result |
| `~`      | Bitwise NOT              | `~a`         | Bitwise result |
| `<<`     | Left shift               | `a << 2`     | Shifted value  |
| `>>`     | Right shift              | `a >> 2`     | Shifted value  |

**Notes:**
- Operate on binary representations of integers.
- Useful for low-level operations.

---

### Membership Operators

| Operator   | Description                    | Example           | Result         |
|------------|--------------------------------|-------------------|----------------|
| `in`       | Value present in sequence      | `'x' in list`     | `True`/`False` |
| `not in`   | Value not present in sequence  | `'x' not in list` | `True`/`False` |

**Notes:**
- Used to check presence in lists, tuples, strings, etc.

---

### Identity Operators

| Operator   | Description                                | Example           | Result         |
|------------|--------------------------------------------|-------------------|----------------|
| `is`       | Same object in memory                      | `a is b`          | `True`/`False` |
| `is not`   | Not the same object in memory              | `a is not b`      | `True`/`False` |

**Notes:**
- Check if two variables refer to the same object (not just equal values).

---

#### Example Usage

```python
a = 10
b = 3
print(a + b)      # 13 (Arithmetic)
print(a ** b)     # 1000 (Arithmetic)
print(a > b)      # True (Comparison)
print(a is b)     # False (Identity)
print(a in [1, 10, 100])  # True (Membership)
```

---

### Operators Not Present in Python

Some operators found in other programming languages are not available in Python:

- **Increment (`++`) and Decrement (`--`) Operators:** Python does not support `++` or `--` for increasing or decreasing variable values. Use `a += 1` or `a -= 1` instead.
- **Ternary (`?:`) Operator:** Python uses a different syntax for conditional expressions: `x if condition else y`.
- **Compound Bitwise Assignment Operators like `&=`, `|=`, `^=`, `<<=`, `>>=`:** These are supported in Python, but some languages have additional compound operators not present in Python.
- **Pointer and Address Operators (`*`, `&` as in C/C++):** Python does not use pointers or direct memory address manipulation.

---
## Notes on `if` and `elif` Statements

- The `if` statement is used to execute a block of code only if a specified condition is `True`.
- The `elif` (short for "else if") statement allows you to check multiple expressions for `True` and execute a block of code as soon as one of the conditions is `True`.
- You can have multiple `elif` statements after an `if`.
- The `else` statement can be used at the end to execute code if none of the previous conditions are `True`.
- Indentation is required to define the blocks of code under each condition.

**Example:**
```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```
## Switch Statement in Python

Python does not have a built-in `switch` or `case` statement like some other languages (e.g., C, Java). Instead, you can achieve similar functionality using `if-elif-else` chains or by using dictionaries to map cases to actions.

**Example using `if-elif-else`:**
```python
value = 2
if value == 1:
    print("One")
elif value == 2:
    print("Two")
elif value == 3:
    print("Three")
else:
    print("Other")
```

**Example using a dictionary (recommended for many cases):**
```python
def switch_case(value):
    return {
        1: "One",
        2: "Two",
        3: "Three"
    }.get(value, "Other")

print(switch_case(2))  # Output: Two
```

**Note:**  
Starting from Python 3.10, the `match` statement (structural pattern matching) provides similar functionality to a switch-case:

```python
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")
```
## Iterative Statements in Python

Iterative statements (loops) are used to execute a block of code repeatedly as long as a condition is met. Python provides two main types of loops: `while` and `for`.

### `while` Loop

The `while` loop executes its block as long as the condition is `True`.

**Syntax:**
```python
while condition:
    # code block
```

**Example:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### `for` Loop

The `for` loop iterates over a sequence (such as a list, tuple, string, or range).

**Syntax:**
```python
for variable in sequence:
    # code block
```

**Example:**
```python
for i in range(5):
    print(i)
```

### `break` and `continue`

- `break` exits the loop immediately.
- `continue` skips the rest of the current iteration and moves to the next.

**Example:**
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### `else` with Loops

An optional `else` block can be added to loops. It executes if the loop completes normally (not terminated by `break`).

**Example:**
```python
for i in range(3):
    print(i)
else:
    print("Loop finished")
 
```
## Collections in Python

Python provides several built-in collection data types to store and organize data:
Below are the four main built-in collection types in Python, along with their meanings and key features:

### List
- **Meaning:** An ordered, mutable collection that can hold items of any type.
- **Features:**
    - Allows duplicate elements.
    - Elements can be changed, added, or removed.
    - Defined using square brackets `[]`.

### Tuple
- **Meaning:** An ordered, immutable collection that can hold items of any type.
- **Features:**
    - Allows duplicate elements.
    - Elements cannot be changed after creation.
    - Defined using parentheses `()`.

### Set
- **Meaning:** An unordered, mutable collection of unique elements.
- **Features:**
    - Does not allow duplicate elements.
    - Elements can be added or removed, but not changed.
    - Defined using curly braces `{}`.

### Dictionary
- **Meaning:** An unordered (insertion ordered from Python 3.7+), mutable collection of key-value pairs.
- **Features:**
    - Keys must be unique and immutable; values can be of any type.
    - Allows fast lookup, insertion, and deletion by key.
    - Defined using curly braces `{}` with key-value pairs separated by colons.

    ### 1. List

    - Ordered, mutable, allows duplicate elements.
    - Defined with square brackets `[]`.

    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    print(fruits[1])  # Output: banana
    ```

    ### 2. Tuple

    - Ordered, immutable, allows duplicate elements.
    - Defined with parentheses `()`.

    ```python
    coordinates = (10, 20)
    print(coordinates[0])  # Output: 10
    ```

    ### 3. Set

    - Unordered, mutable, no duplicate elements.
    - Defined with curly braces `{}`.

    ```python
    unique_numbers = {1, 2, 3, 2}
    unique_numbers.add(4)
    print(unique_numbers)  # Output: {1, 2, 3, 4}
    ```

    ### 4. Dictionary

    - Unordered (Python 3.7+: insertion ordered), mutable, key-value pairs.
    - Defined with curly braces `{}` and colons.

    ```python
    person = {"name": "Alice", "age": 25}
    print(person["name"])  # Output: Alice
    person["age"] = 26
    ```

    ---

    **Summary Table:**

    | Type        | Ordered | Mutable | Allows Duplicates | Example Syntax      |
    |-------------|---------|---------|-------------------|---------------------|
    | List        | Yes     | Yes     | Yes               | `[1, 2, 3]`         |
    | Tuple       | Yes     | No      | Yes               | `(1, 2, 3)`         |
    | Set         | No      | Yes     | No                | `{1, 2, 3}`         |
    | Dictionary  | Yes*    | Yes     | Keys: No, Values: Yes | `{"a": 1, "b": 2}` |

    \*Dictionaries preserve insertion order from Python 3.7 onwards.

    --- 
## Handling Regular Expressions in Python

Regular expressions (regex) are used for searching, matching, and manipulating text based on patterns. Python provides the `re` module to work with regular expressions.

### Basic Usage

```python
import re

pattern = r"\d+"
text = "There are 24 apples and 7 oranges."
matches = re.findall(pattern, text)
print(matches)  # Output: ['24', '7']
```

### Common Functions in `re` Module

- `re.match(pattern, string)`: Checks for a match only at the beginning of the string.
- `re.search(pattern, string)`: Searches the string for a match.
- `re.findall(pattern, string)`: Returns all non-overlapping matches as a list.
- `re.sub(pattern, repl, string)`: Replaces matches with a string.

---

### Regular Expression Wildcard Characters

| Character | Description                                 | Example      | Matches                |
|-----------|---------------------------------------------|--------------|------------------------|
| `.`       | Any character except newline                | `a.c`        | `abc`, `a1c`, `a-c`    |
| `^`       | Start of string                             | `^abc`       | `abc` at start         |
| `$`       | End of string                               | `abc$`       | `abc` at end           |
| `*`       | 0 or more repetitions of preceding pattern  | `ab*`        | `a`, `ab`, `abb`       |
| `+`       | 1 or more repetitions of preceding pattern  | `ab+`        | `ab`, `abb`            |
| `?`       | 0 or 1 repetition of preceding pattern      | `ab?`        | `a`, `ab`              |
| `{n}`     | Exactly n repetitions                      | `a{3}`       | `aaa`                  |
| `{n,}`    | n or more repetitions                      | `a{2,}`      | `aa`, `aaa`, ...       |
| `{n,m}`   | Between n and m repetitions                | `a{1,3}`     | `a`, `aa`, `aaa`       |
| `[]`      | Any one character in set                   | `[abc]`      | `a`, `b`, or `c`       |
| `[^]`     | Any one character not in set               | `[^abc]`     | Not `a`, `b`, or `c`   |
| `|`       | Alternation (OR)                           | `a|b`        | `a` or `b`             |
| `\d`      | Any digit (0-9)                            | `\d`         | `0` to `9`             |
| `\D`      | Any non-digit                              | `\D`         | Any non-digit character|
| `\w`      | Any word character (alphanumeric or _)      | `\w`         | `a-z`, `A-Z`, `0-9`, `_`|
| `\W`      | Any non-word character                     | `\W`         | Not `a-z`, `A-Z`, `0-9`, `_`|
| `\s`      | Any whitespace character                   | `\s`         | Space, tab, newline    |
| `\S`      | Any non-whitespace character               | `\S`         | Any non-whitespace     |

**Note:** Use raw strings (prefix with `r`) for regex patterns to avoid issues with escape sequences.

--- 
## Ternary Operator Alternative in Python

Python does not have the `?:` ternary operator found in languages like C or Java. Instead, it uses a conditional expression with the syntax:

```python
value_if_true if condition else value_if_false
```

**Example:**
```python
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Odd
```

This provides a concise way to assign a value based on a condition.
## Loop Expressions (List Comprehensions)

Python provides a concise way to create lists using loop expressions, known as list comprehensions. They allow you to generate a new list by applying an expression to each item in an iterable, optionally filtering items with a condition.

**Syntax:**
```python
[expression for item in iterable if condition]
```

**Examples:**
```python
# Create a list of squares from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

**Other Comprehensions:**
- **Set comprehension:** `{x for x in iterable}`
- **Dictionary comprehension:** `{k: v for k, v in iterable}`
- **Generator expression:** `(expression for item in iterable)`

List comprehensions are often more readable and efficient than using loops to build l

## Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and improve readability.

### Defining a Function

Use the `def` keyword to define a function:

```python
def greet(name):
    print(f"Hello, {name}!")
```

### Calling a Function

Invoke the function by its name and pass required arguments:

```python
greet("Alice")  # Output: Hello, Alice!
```

### Function Arguments

- **Positional arguments:** Passed in order.
- **Keyword arguments:** Passed by name.
- **Default arguments:** Provide a default value.
- **Variable-length arguments:** Use `*args` for positional and `**kwargs` for keyword arguments.

```python
def add(a, b=0):
    return a + b

print(add(5))        # Output: 5
print(add(5, 3))     # Output: 8

def print_args(*args):
    print(args)

print_args(1, 2, 3)  # Output: (1, 2, 3)
```

### Return Statement

Use `return` to send a value back from the function:

```python
def square(x):
    return x * x

result = square(4)  # result is 16
```

### Lambda Functions

Anonymous, single-expression functions:

```python
double = lambda x: x * 2
print(double(5))  # Output: 10
```

---

**Summary Table:**

| Feature            | Syntax Example                          |
|--------------------|-----------------------------------------|
| Define function    | `def func():`                           |
| Call function      | `func()`                                |
| Return value       | `return value`                          |
| Default argument   | `def func(a=1):`                        |
| Variable arguments | `def func(*args, **kwargs):`            |
| Lambda function    | `lambda x: x + 1`                       |

---

## Functions with Variable Number of Parameters

Python allows you to define functions that accept a variable number of arguments using `*args` for positional arguments and `**kwargs` for keyword arguments.

### Using `*args`

- Collects extra positional arguments as a tuple.

```python
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)  # Output: 1 2 3
```

### Using `**kwargs`

- Collects extra keyword arguments as a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# Output:
# name: Alice
# age: 25
```

### Combining Both

You can use both in the same function (with `*args` before `**kwargs`):

```python
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, a=3, b=4)
# Output:
# args: (1, 2)
# kwargs: {'a': 3, 'b': 4}
```

## Callback Functions in Python

A callback function is a function that is passed as an argument to another function and is intended to be called after a certain event or action occurs. Callbacks are commonly used for event handling, asynchronous programming, and customizing behavior.

### Defining and Using a Callback

You can pass a function as an argument to another function:

```python
def process_data(data, callback):
    # Do something with data
    result = data.upper()
    # Call the callback function with the result
    callback(result)

def print_result(output):
    print("Processed:", output)

process_data("hello", print_result)
# Output: Processed: HELLO
```

### Using Lambda as a Callback

You can also use a lambda function as a callback:

```python
process_data("world", lambda x: print("Lambda:", x))
# Output: Lambda: WORLD
```

**Note:**  
Any function that can be called (including lambdas and built-in functions) can be used as a callback in Python.

## The `map()` Function in Python

The `map()` function applies a given function to each item of an iterable (like a list or tuple) and returns a map object (which can be converted to a list, set, etc.).

**Syntax:**
```python
map(function, iterable, ...)
```

- `function`: The function to apply to each item.
- `iterable`: One or more iterables whose items are passed to the function.

**Example:**
```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

**With Multiple Iterables:**
```python
a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))  # Output: [5, 7, 9]
```

**Note:**  
`map()` returns an iterator in Python 3. Use `list()` or `set()` to get the results.

## The `filter()` Function in Python

The `filter()` function constructs an iterator from elements of an iterable for which a function returns `True`.

**Syntax:**
```python
filter(function, iterable)
```
- `function`: A function that returns `True` or `False` for each element.
- `iterable`: The sequence to filter.

**Example:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]
```

**Note:**  
`filter()` returns an iterator in Python 3. Use `list()` or `set()` to get the results.

## The `reduce()` Function in Python

The `reduce()` function applies a specified function cumulatively to the items of an iterable, reducing the iterable to a single value. It is available in the `functools` module.

**Syntax:**
```python
from functools import reduce

reduce(function, iterable[, initializer])
```
- `function`: A function that takes two arguments and returns a single value.
- `iterable`: The sequence to process.
- `initializer` (optional): A starting value.

**Example:**
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

**With an Initializer:**
```python
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial)  # Output: 20
```

**Note:**  
Use `reduce()` when you need to combine all elements of an iterable into a single result, such as summing or multiplying all items.

## Exception Handling in Python

Exception handling allows you to manage errors gracefully and prevent your program from crashing unexpectedly. Python uses `try`, `except`, `else`, and `finally` blocks for exception handling.

### Basic Syntax

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero.")
```

### Catching Multiple Exceptions

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid input or type.")
```

### Using `else` and `finally`

- `else` runs if no exception occurs.
- `finally` always runs (for cleanup actions).

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number.")
else:
    print("You entered:", num)
finally:
    print("Execution complete.")
```

### Raising Exceptions

Use `raise` to trigger exceptions manually.

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
```

---

**Summary Table:**

| Block     | Purpose                                      |
|-----------|----------------------------------------------|
| `try`     | Wrap code that may raise exceptions          |
| `except`  | Handle specific exceptions                   |
| `else`    | Run if no exception occurs                   |
| `finally` | Always run (cleanup, closing files, etc.)    |

--- 
## User Defined Exceptions in Python

Python allows you to define your own custom exception classes by inheriting from the built-in `Exception` class (or one of its subclasses). This is useful when you want to signal specific error conditions in your code.

### Defining a Custom Exception

```python
class MyCustomError(Exception):
    """Custom exception for specific error cases."""
    pass
```

### Raising and Handling a Custom Exception

```python
def check_positive(number):
    if number < 0:
        raise MyCustomError("Number must be positive")
    return number

try:
    check_positive(-5)
except MyCustomError as e:
    print("Caught custom exception:", e)
```

**Notes:**
- You can add custom initialization or attributes to your exception class if needed.
- Custom exceptions help make your code more descriptive and easier to debug.
- It's common to end custom exception class names with `Error`.

--- 
## Object Oriented Programming (OOP) in Python

Object Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). Python supports OOP and allows you to define your own classes and create objects.

### Key Concepts

- **Class:** A blueprint for creating objects.
- **Object:** An instance of a class.
- **Attribute:** A variable that belongs to an object or class.
- **Method:** A function that belongs to an object or class.
- **Inheritance:** Mechanism to create a new class from an existing class.
- **Encapsulation:** Hiding internal details and showing only necessary features.
- **Polymorphism:** Ability to use a common interface for different data types.

### Defining a Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

### Creating Objects

```python
p1 = Person("Alice", 30)
p1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

### Inheritance

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_id(self):
        print(f"Student ID: {self.student_id}")

s1 = Student("Bob", 20, "S123")
s1.greet()        # Inherited method
s1.display_id()   # Output: Student ID: S123
```

### Encapsulation

- Prefix an attribute with `_` (single underscore) to indicate it is intended as "protected".
- Prefix with `__` (double underscore) to make it "private" (name mangling).

```python
class Example:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
```

### Polymorphism

Different classes can define methods with the same name, and you can use them interchangeably.

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())  # Output: Woof!
animal_sound(Cat())  # Output: Meow!
```

---

**Summary Table:**

| Concept        | Description                                      | Example Syntax                |
|----------------|--------------------------------------------------|-------------------------------|
| Class          | Blueprint for objects                            | `class MyClass:`              |
| Object         | Instance of a class                              | `obj = MyClass()`             |
| Attribute      | Variable in class/object                         | `self.attr = value`           |
| Method         | Function in class                                | `def method(self):`           |
| Inheritance    | Derive class from another                        | `class Sub(Base):`            |
| Encapsulation  | Hide internal details                            | `_protected`, `__private`     |
| Polymorphism   | Same interface, different implementations        | `animal.speak()`              |

---
## Creating Modules in Python

A module in Python is simply a file containing Python code (functions, classes, variables) that can be imported and reused in other programs.

### Creating a Module

1. **Write your code in a `.py` file.**  
    Example: `mymodule.py`
    ```python
    # mymodule.py
    def greet(name):
         print(f"Hello, {name}!")
    ```

2. **Import the module in another Python file.**
    ```python
    import mymodule

    mymodule.greet("Alice")  # Output: Hello, Alice!
    ```

### Importing Specific Items

You can import specific functions, classes, or variables:
```python
from mymodule import greet

greet("Bob")
```

### Module Search Path

Python searches for modules in:
- The current directory
- Directories listed in `sys.path`
- Standard library locations

### The `__name__ == "__main__"` Idiom

To allow code to run when the module is executed directly, but not when imported:
```python
# mymodule.py
def greet(name):
     print(f"Hello, {name}!")

if __name__ == "__main__":
     greet("World")
```

### Packages

A package is a directory containing an `__init__.py` file and one or more module files. Import modules from packages using dot notation:
```
mypackage/
     __init__.py
     module1.py
```
```python
from mypackage import module1
```

**Summary:**  
- Modules help organize and reuse code.
- Use `import` to access code from other modules.
- Group related modules in packages for better structure.

## File Handling in Python

File handling allows you to read from and write to files on disk. Python provides built-in functions and the `open()` function for file operations.

### Opening a File

Use `open(filename, mode)` to open a file:
- `'r'`: Read (default)
- `'w'`: Write (creates/truncates)
- `'a'`: Append
- `'b'`: Binary mode (e.g., `'rb'`, `'wb'`)
- `'x'`: Create (fails if file exists)

```python
f = open("example.txt", "r")
```

### Reading from a File

```python
with open("example.txt", "r") as f:
    content = f.read()         # Read entire file
    # content = f.readline()   # Read one line
    # content = f.readlines()  # Read all lines into a list
```

### Writing to a File

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])
```

### Appending to a File

```python
with open("output.txt", "a") as f:
    f.write("Another line\n")
```

### Closing a File

Files are automatically closed when using `with`. Otherwise, use `f.close()`.

### Example: Copying File Contents

```python
with open("input.txt", "r") as src, open("output.txt", "w") as dst:
    for line in src:
        dst.write(line)
```

### Checking File Existence

```python
import os
if os.path.exists("example.txt"):
    print("File exists")
```

---

**Summary Table:**

| Mode | Description           |
|------|-----------------------|
| `'r'`  | Read (default)      |
| `'w'`  | Write (overwrite)   |
| `'a'`  | Append              |
| `'b'`  | Binary mode         |
| `'x'`  | Create, fail if exists |

---

**Note:** Always use `with` for file operations to ensure files are properly closed.
## Working with Databases in Python

Python provides several libraries for interacting with databases. For MySQL, the most commonly used library is `mysql-connector-python` or `PyMySQL`.

### Installing MySQL Connector

Install the connector using pip:

```bash
pip install mysql-connector-python
```

### Connecting to a MySQL Database

```python
import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
```

### Basic Operations

- **Insert Data:**
    ```python
    cursor.execute("INSERT INTO your_table (col1, col2) VALUES (%s, %s)", (val1, val2))
    conn.commit()
    ```
- **Update Data:**
    ```python
    cursor.execute("UPDATE your_table SET col1 = %s WHERE id = %s", (new_val, id_val))
    conn.commit()
    ```
- **Delete Data:**
    ```python
    cursor.execute("DELETE FROM your_table WHERE id = %s", (id_val,))
    conn.commit()
    ```

### Using Context Manager

You can use `with` statements for automatic resource management:

```python
import mysql.connector

with mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table")
        for row in cursor.fetchall():
            print(row)
```

---

**Note:**  
- Always handle exceptions using `try-except` blocks for production code.
- Never hardcode credentials in source files; use environment variables or configuration files.

---

**Summary Table:**

| Operation      | Example Syntax                                      |
|----------------|-----------------------------------------------------|
| Connect        | `mysql.connector.connect(...)`                      |
| Create Cursor  | `conn.cursor()`                                     |
| Execute Query  | `cursor.execute("SQL", params)`                     |
| Fetch Results  | `cursor.fetchall()` / `cursor.fetchone()`           |
| Commit Changes | `conn.commit()`                                     |
| Close          | `cursor.close()`, `conn.close()`                    |

---

## Connecting Python to AWS

Python can interact with AWS (Amazon Web Services) using the `boto3` library, which is the official AWS SDK for Python. With `boto3`, you can manage AWS services such as S3, EC2, DynamoDB, Lambda, and more.

### Installing `boto3`

Install the library using pip:

```bash
pip install boto3
```

### Configuring AWS Credentials

You need AWS access keys to authenticate. Configure them using the AWS CLI or by setting environment variables:

```bash
aws configure
```

Or set environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_region
```

### Example: Connecting to S3 and Listing Buckets

```python
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
```

### Example: Uploading a File to S3

```python
import boto3

s3 = boto3.client('s3')
s3.upload_file('local_file.txt', 'your-bucket-name', 'remote_file.txt')
```

### Example: Connecting to EC2 and Listing Instances

```python
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['State']['Name'])
```

---

**Note:**  
- Always use IAM roles or environment variables for credentials, not hardcoded values.
- Refer to the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for more AWS service examples.

--- 