'''Counters
OrderedDict
DefaultDict
ChainMap
NamedTuple
DeQue
'''
'''
import collections
collections.Counter()


import collections as co
co.Counter

from collections import *

from collections import Counter
Counter()
'''

# Counter:

# A Python program to show different ways to create Counter
from collections import Counter
	
# With sequence of items
print(Counter(['B','B','A','B','C','A','B',
			'B','A','C']))
	
# with dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
	
# with keyword arguments
print(Counter(A=3, B=5, C=2))

# DefaultDict

from collections import defaultdict

# Create a defaultdict with default value as 0
numbers = defaultdict(int)

numbers['one'] = 1
numbers['two'] = 2

print(numbers['one'])  # Output: 1
print(numbers['two'])  # Output: 2
print(numbers['three'])  # Output: 0 (default value)
print(numbers['ABC'])

print(numbers)  # Output: defaultdict(<class 'int'>, {'one': 1, 'two': 2, 'three': 0})


# ChainMap

# Python program to demonstrate ChainMap
		
from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2} # d1['a']
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)
print(c['a'])

#NamedTuple

# Python code to demonstrate namedtuple()
	
from collections import namedtuple
	
# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
	
# Adding values
S = Student('Nandini','19','2541997')
	
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
	
# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)

# Deque

# Python code to demonstrate working of
# append(), appendleft()
	

from collections import deque
	
# initializing deque
de = deque([1,2,3])
	
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
	
# printing modified deque
print ("The deque after appending at right is : ")
print (de)
	
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
	
# printing modified deque
print ("The deque after appending at left is : ")
print (de)

de.popleft()
print(de)