# strings2.py
# Demonstration of common string functions in Python

s = "  This is a cool world!  everything seems to be fine.  "

# Remove leading/trailing whitespace
print("strip():", s.strip())

# Convert to uppercase
print("upper():", s.upper())

# Convert to lowercase
print("lower():", s.lower())

# Replace substring
print("replace():", s.replace("world", "Python"))

# Find substring
print("find():", s.find("World"))

# Split into list
print("split():", s.strip().split(" "))

# Join list into string
words = ["Python", "is", "fun"]
print("join():", " ".join(words))

# Check if string starts with
print("startswith():", s.startswith("  Hello"))

# Check if string ends with
print("endswith():", s.endswith("!  "))

# Count occurrences
print("count():", s.count("l"))