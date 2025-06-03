for x in range(2,1000):
    flag = True
    for y in range(2, x//2):
        if x % y == 0:
            flag= False
            break
    if flag:
        print(x, end=' ')
print("\n Using while loop to find prime numbers between 2 and 1000:")
x = 2 #initialization
while x < 1000: #condition
    flag = True
    y = 2
    while y < x // 2:
        if x % y == 0:
            flag = False
            break
        y += 1 #increment
    if flag:
        print(x, end=' ')
    x += 1