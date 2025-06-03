# Demonstrate formatted output: binary, octal, hexadecimal, and integer equivalents

number = 42

print(f"Decimal     : {number}")
print(f"Binary      : {bin(number)}")
print(f"Octal       : {oct(number)}")
print(f"Hexadecimal : {hex(number)}")

# Alternatively, using format specifiers
print("\nUsing format specifiers:")
print("Binary      : {0:b}".format(number))
print("Octal       : {0:o}".format(number))
print("Hexadecimal : {0:x}".format(number))

# Print values as literals in their respective bases
binary_literal = 0b101010
octal_literal = 0o52
hex_literal = 0x2a

print("\nLiterals as their respective bases:")
print(f"Binary literal      : {bin(binary_literal)}")
print(f"Octal literal       : {oct(octal_literal)}")
print(f"Hexadecimal literal : {hex(hex_literal)}")