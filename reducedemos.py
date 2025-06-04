from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5,6,7,8,9,10]))  
print(reduce(lambda x, y: x if x > y else y, [435,43,3456,4345,34, 345, 456, 2345, 234]))

