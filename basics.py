
# Python 
##

# My Road to Python
# Approx 2008, internship at small company
# No matlab + commercial CFD code
##

# Why Python
# Simple to learn (hard to master?)
# Clean Syntax, no unneeded cruft
# Batteries included, numerous modules on pypi
# Many Python API's e.g. Paraview
##

# Active community
# https://www.youtube.com/watch?v=OSGv2VnC0go # Hettinger - Beautiful Code
# https://www.youtube.com/watch?v=RrPZza_vZ3w # Beazly Beginner Tutorial
# https://www.youtube.com/watch?v=xe_ATRmw0KM # Perez - Ipython
# https://www.youtube.com/watch?v=w26x-z-BdWQ # Kinney - Pandas
# https://www.youtube.com/watch?v=EnSu9hHGq5o # Batchelder
# https://www.youtube.com/watch?v=FxSsnHeWQBY # Batchelder
##

# Which Pythons
# Language definitions: python2.7 python3.x

# Implementations c-python
#                 ipython 
# Install it:
# sudo apt-get install ipython ipython-notebook python-pip
##
# Data Structures - Lists
empty_list  = []

example_list = [1,2,3,"a","b","c"] #extremely important

example_persons = ["Alice", 1.60, "Bob", 1.80] # but don't do this

example_persons_objects =  [
        ("Alice", 1.60), # or use custom class 
        ("Bob", 1.80),   # e.g Person("Alice",1.60) ..
    ] 
##
# Data Structures - Tuples
# Tuples are just fixed size lists

example_tuple = (1,2)
a,b = (1,2) # Tuple unpacking
example_tuple2 = 3,4
## 

# Data Structures - Dictionaries
example_dict = {'a':'abc', 1:123}

# Warning standard dictionaries are unordered
##

# Control Flow - Loops
for el in example_list:
    print el

# instead of range(len((example_list))
for i,el in enumerate(example_list):
    print i,el
##

# Control Flow - List Comprehensions
l1 = [el for el in range(20)]
l2 = [el*2 for el in range(20)]
l3 = [el*2 for el in range(20) if el > 10]
l4 = [el*2 for el in range(20) if el < 10]
##

# Control Flow - zips
#for l3i,l4i in zip(l3,l4)
#        print l3i,l4i
##

# Functions
def func(a,b):
    """ a function """
    return a+b

# Indentation matters
# After colon a new indentation level is needed
# Function ends with end of indentation level
##

# Function Returns and Arguments
# Function can return multiple variables
def func_2(a,b):
    """ a function """
    return 2*a,2*b
## 

# Best Practise Functions

# Write functions to build logical units

# Defining a functions gives a comment for 
# free by its name

# Seperate responsibilites

# Allow unit tests
##
