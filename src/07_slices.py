"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
sliceObj = slice(1,2)
# Output the second element: 4:
print(a[sliceObj])

# Output the second-to-last element: 9
sliceObj2 = slice(4,5)
print(a[sliceObj2])

# Output the last three elements in the array: [7, 9, 6]
array = slice(3,6)
print(a[array])

# Output the two middle elements in the array: [1, 7]
array1 = slice(2,4)
print(a[array1])

# Output every element except the first one: [4, 1, 7, 9, 6]
array2 = slice(1,6)
print(a[array2])

# Output every element except the last one: [2, 4, 1, 7, 9]
array3 = slice(0,5)
print(a[array3])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
string = slice(7,12)
print(s[string])