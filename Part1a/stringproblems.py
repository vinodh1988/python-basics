

# Example usage:
string = input("Enter a string: ")
if string.lower() == string.lower()[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

string= input("Enter a string to find the largest word: ")
words = string.split()
if words:
    largest = max(words, key=len) 
    print("Largest word:", largest)
else:
    print("No words found.")
