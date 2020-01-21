"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open("foo.txt", "r")
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

file_name = "bar.txt"
f = open(file_name, "w+")
print(f.write("hello love me\n"))
print(f.write("What's going on\n"))
print(f.write("yeah yeah\n"))
print(f.read())
f.close()
# *** question why is this printing 
# out as int total of number ***


file_name2 = open("uper.text", "w")
file_name2 = open("uper.text", "a")
textList = ["hello", "what did you do", "how did it go"]

file_name2 =open("uper.text", "w+")
for line in textList:
    file_name2.write(line)
    file_name2.write("\n")
file_name2.close()

f = open("uper.text", "r")
print(f.read())
f.close()




