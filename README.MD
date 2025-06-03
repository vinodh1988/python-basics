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