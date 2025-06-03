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