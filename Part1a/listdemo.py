lista = [34,56,78,90,12,34,56,78,90,12,34,56,78,90]
for x in lista:
    print(x, end=' ')
print("\nsize of list:", len(lista))
print("8th element:", lista[7])  # Accessing the 8th element (index 7)
print("List a:", lista)
lista.append(100)  # Adding an element to the end of the list
print("\nAfter appending 100:", lista)
lista.insert(5, 200)  # Inserting 200 at index 5
print("After inserting 200 at index 5:", lista)
lista.extend([45, 67, 89])  # Extending the list with multiple elements
print("After extending with [45, 67, 89]:", lista)
del lista[2]  # Deleting the element at index 2
print("After deleting element at index 2:", lista)

print("checking whether 12 is present in the list:", 12 in lista)  # Checking if 12 is in the list

print("List from 1 to 10:", lista[1:11])  # Creating a list from 1 to 10
print("List from 1 to 10:", lista[0:18:2])
print("Reversed list:", lista[::-1])  # Reversing the list
print("Sorted list:", sorted(lista))  # Sorting the list
