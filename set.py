setx={43,356,34,35,34,56,78,90,12,34,56,78,90,12,34,56,78,90}
print("setx:", setx)
print("Size of set:", len(setx))
setx.add(100)  # Adding an element to the set
setx.add(200)  # Adding another element to the set
print("After adding 100 and 200:", setx)
setx.remove(34)  # Removing an element from the set
print("After removing 34:", setx)
#print("Accessing an element (not possible in sets):"+setx[2]) #error