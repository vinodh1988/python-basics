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