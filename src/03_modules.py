"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE


# this will not print out the arguments on both lines
print("This is the name of the script", sys.argv[0])

#looping through
for a in sys.argv:
    print(a)
    print("The arguments are loops: ", str(a))

# access command line arguments
print("Number of arguments", len(sys.argv))
#list commands line by line
print("The arguments are: ", str(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
print("The OS I'm using",sys.platform.capitalize())

# Print out the version of Python you're using:
# YOUR CODE HERE
print("The version of Python I'm using is", sys.version)


import os
# # See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("The current process ID", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("The current working director is", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("The maching loing name is", os.getlogin())