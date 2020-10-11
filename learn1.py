# Array


def printArray(arr):
    for a in arr:
        print(a)


from array import *

val = array("i", [1, 2, 3, 4, 5, 6])

# print(val.index(2))

"""
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 byte
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytes
d	Represents floating point of size 8 bytes
"""

# INSERT
val.insert(1, 7)
val.insert(3, 7)
# printArray(val)

# DELETE
val.remove(7)  # first instance of value 7 will get deleted
# printArray(val)

# UPDATE
val[5] = 9
# printArray(val)

# DELETE last element
val.pop()

# Add value at the end of the array
val.append(11)

printArray(val)

