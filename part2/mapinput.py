#setA=set(map(lambda x:x,input("enter numbers seperated by space: ").split()))
setA=set(map(int,input("enter numbers seperated by space: ").split()))
setB=set(map(int,input("enter numbers seperated by space: ").split()))

print(setA)
print(setB)

setC=setA.intersection(setB)
print(setC)