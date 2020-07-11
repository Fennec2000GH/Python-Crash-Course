# https://www.tutorialspoint.com/jython/index.htm
# c:\Users\qcaij\OneDrive - University of Florida\Files\College\Coursework\Summer 2020\CIS 4930 - Special Topics - Performant Programming in Python\Python-Crash-Course\src\Third Party Modules\Jython\jython_tutorial.py
########################################################################################################################
# Importing Java Libraries

from java.util import Date

d = Date()
print(d)

import HelloWorld

h = HelloWorld()
h.hello()
h.hello("Isaac")

########################################################################################################################
# Variables and Data Types

x = 10
print(type(x))
x = "hello"
print(type(x))

# Jython Numbers
x = 42  # int
print(type(x))
x = 1234567890L  # long
print(type(x))
x = 42.42  # float
print(type(x))
x = 120 + 42j  # complex
print(type(x))

# Jython Strings
string = 'Hello how are you?'
print(type(string))
string = "Hello how are you?"
print(type(string))
string = """this is a long string that is made up of several lines and non-printable
characters such as TAB ( \t ) and they will show up that way when displayed. NEWLINEs
within the string, whether explicitly given like this within the brackets [ \n ], or just
a NEWLINE within the variable assignment will also show up."""
print(type(string))

# Jython Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# Jython tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])

# Jython Dictionary
dict = {'011': 'New Delhi', '022': 'Mumbai', '033': 'Kolkata', 'Age': 25}
print("dict['011']: ", dict['011'])
print("dict['Age']: ", dict['Age'])

########################################################################################################################

import java.util.ArrayList as ArrayList

arr = ArrayList()
arr.add(10)
arr.add(20)
print("ArrayList: ", arr)
arr.remove(10)  #remove 10 from arraylist
arr.add(0, 5)  #add 5 at 0th index
print("ArrayList: ", arr)
print("element at index 1:", arr.get(1))  #retrieve item at index 1
arr.set(0,100)  #set item at 0th index to 100
print("ArrayList: ", arr)

# Jarray Class
from jarray import array

my_seq = (1, 2, 3, 4, 5)
arr1 = array(my_seq, 'i')
print(arr1)
myStr = "Hello Jython"
arr2 = array(myStr, 'c')
print(arr2)
