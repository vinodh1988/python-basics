# createtextfile.py

# Specify the file name
filename = "example.txt"

# Data to write
data = "Hello, this is a sample text file.\nWelcome to Python programming!"

# Open the file in write mode and write data
with open(filename, "w") as file:
    file.write(data)

print(f"Data written to {filename}")