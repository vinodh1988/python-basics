a=13
b=7

#a = 1101
#b = 0111
#& = 0101  => 5
#| = 1111  => 15
#^ = 1010  => 10

print("a =", a, ", b =", b, "=> a & b =", a & b)
print("a =", a, ", b =", b, "=> a | b =", a | b)
print("a =", a, ", b =", b, "=> a ^ b =", a ^ b)

# a= 1101
# a >> 2
# a = 0011  => 3
# a << 2
# a = 110100  => 52

print("a =", a, ", b =", b, "=> a >> 2 =", a >> 2)
print("a =", a, ", b =", b, "=> a << 2 =", a << 2)
# size of int in Python is 4 bytes

# 32 bit representation of 13 is 00000000 00000000 00000000 00001101
# left most bit is the sign bit
# if it is 0, the number is positive , if it is 1, the number is negative
# ~ on 12 => 11111111 11111111 11111111 11110010
print("a=",a, ",~a =", ~a)
c=-18
# 32 bit representation of -18 is 11111111 11111111 11111111 11101110
print("c=",c, ",~c =", ~c)