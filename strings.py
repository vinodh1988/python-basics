value="internationalization"

for x in value:
    print(x, end=' ')

print("\n")
for x in value[0:5]:
    print(x, end=' ')

print("\n")
for x in value[0:10:2]:
    print(x, end=' ')

print("\n")
for x in value[::-1]:
    print(x, end=' ')

# [lower:upper:step]  --> slicing
print("\n\nSlicing examples:")
print(value[0:5])  # 'inter'
print(value[0:10:2])  # 'itain'
print(value[::-1])  # 'noitazinretni'