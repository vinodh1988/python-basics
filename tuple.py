tuplea=(43,34,56,78,90,12,34,56,78,90,12,34,56,78,90)
for x in tuplea:
    print(x, end=' ')

print("\nSize of tuple:", len(tuplea))
print("8th element:", tuplea[7])  # Accessing the 8th element (index 7)
#tuplea.append(100)  # Tuples are immutable, so this will raise an error