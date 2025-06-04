listx=[34,56,34,6,483,35,99,124,455,256,242,12,1,5,8999,34,678,366]

threedigits = [ x if x>=100 and x<=999 else 0 for x in listx ]

print("Three digit numbers in the list are: ", threedigits)

names=["Alice", "Bob", "Charlie", "David", "Eve"]

length_of_names = { name: len(name) for name in names}

print("Length of names in the list are: ", length_of_names)

threedigits = [ x  for x in listx if x>=100 and x<=999 ]

print("Three digit numbers in the list are: ", threedigits)