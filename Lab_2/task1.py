#BOOLEANS

#example1
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

#example2
# a = 200
# b = 33

# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

#example3
# print(bool("Hello"))
# print(bool(15))

#example4
# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

#example5
# print(bool("abc"))
# print(bool(123))
# print(["apple", "cherry", "banana"])

#example6
# bool(False)
# bool(None)
# bool(0)
# bool(())
# bool("")
# bool([])
# bool({})

#example7
# class myclass():
#     def __len__(self):
#         return 0
    
# myobj = myclass()
# print(bool(myobj))

# example8
# def myFunction():
#     return True

# print(myFunction())

#example9
# def myFunction():
#     return True

# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# example9
# x = 200
# print(isinstance(x, int))

#exercise1
# print(10 > 9)
# True

# #exercise2
# print(10 == 9)
# False

# #exercise3
# print(10 < 9)
# False

# #exercise4
# print(bool("abc"))
# True

# #exercise5
# print(bool(0))
# False



#OPERATORS

#example
# print(10+5)

#example
# x = 5
# y = 3
# print(x + y)

#example
# x = 5
# y = 3
# print(x - y)

#example
# x = 5
# y = 3
# print(x * y)

#example
# x = 12
# y = 3
# print(x / y)

#example
# x = 5
# y = 2
# print(x % y)

#example
# x = 2
# y = 5
# print(x ** y) #2*2*2*2*2

#example
# x = 15
# y = 2
# print(x // y)
#the floor division // rounds the result down to the nearest whole number



#assingment operators

#example
# x = 5
# print(x)

#example
# x = 5
# x += 3
# print(x)

#example
# x = 5
# x -= 3
# print(x)

#example
# x = 5
# x /= 3
# print(x)

#example
# x = 5
# x %= 3
# print(x)

# example
# x = 5
# x //= 3
# print(x)

# example
# x = 5
# x **=3
# print(x)

# AND
# x = 5
# x &= 3
# print(x)
#output 1 

#OR
# x = 5
# x |= 3
# print(x) 
# outputs 7 

#XOR 
# x = 5
# x ^= 3
# print(x)
# outputs 6


# comparison operators

# equal
# x = 5
# y = 3
# print(x == y)

# not equal
# x = 5
# y = 3
# print(x != y)

# greater than
# x = 5
# y = 3
# print(x > y)

# less than
# x = 5
# y = 3
# print(x < y)

# greater than or equal to
# x = 5
# y = 3
# print(x >= y)

# Less than or equal to
# x = 5
# y = 3
# print(x <= y)



# logical operators

# and
# x = 5
# print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# or
# x = 5
# print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# not
# x = 5
# print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result



# identity operators

# is
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)


# is not
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is not z)
# print(x is not y)
# print(x != y)



# membership operators

# in
# x = ["apple", "banana"]
# print("banana" in x)

# not in
# x = ["apple", "banana"]
# print("pineapple" not in x)



# bitwise operations

# &  AND
# print(6 & 3)

# outputs 2

#|  OR
# print(6 | 3)

# outputs 7

# ^ XOR
# print(6 ^ 3)

# outputs 5
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# ~  NOT
# print(~4)

# outputs -4
# 0 1 
# 1 0

# <<  zero fill left shift
# print(3 << 2)

# outputs 12

"""
Shift left by pushing zeros in from the right and let the leftmost bits fall off
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""

# >> signed right shift
# print(8 >> 2)

# outputs 2

"""
Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""



# operator precedence (order of operations)

#parenthese
# print((6 + 3) - (6 + 3))

#multiplication, division, floor division, and modulus (higher precedence)
# print(100 + 5 * 3)

#addition and substraction
# print(100 - 5 * 3)

# Bitwise left and right shifts (lower precedence)
# print(8 >> 4 - 2)

# outputs 2

# Bitwise AND (lower precedence)
# print(6 & 2 + 1)

# outputs 2

# Bitwise XOR (lower precedence)
# print(6 ^ 2 + 1)

# outputs 5

# Bitwise OR (lower precedence)
# print(6 | 2 + 1)

# outputs 7

# comparisons, identity, and membership operators (lower precedence)
# print(5 == 4 + 1)

# outputs true 

# logical NOT (lower precedence)
# print(not 5 == 5)

# outputs False


# and (higher precedence)
# print(1 or 2 and 3)

# outputs 1

# or (lower precedence)
# print(4 or 5 + 10 or 8)

# outputs 4


#example (addition = substraction)
# print(5 + 4 - 7 + 3)

# outputs 5


#exercise1
# print(10*5)

#exercise2
# print(10/2)

# exercise3
# fruits = ["apple", "banana"]
# if "apple" in fruits:
#     print("Yes, apple is in fruit!")

# exercise4
# if 5 != 10:
#     print("5 and 10 are not equal")

# exercise5
# if 5 == 10 or 4 == 4:
#     print("At least one of the statements is true")




# LISTS

# example

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# duplicates
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# data types
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print(list1)
# print(list2)
# print(list3)

# different data types
# list1 = ["abc", 34, True, 40, "male"]

# print(list1)

# type()
# mylist = ["apple", "banana", "cherry"]

# print(type(mylist))

# outputs <class 'list'>


# list()
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# access list items

# example
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# negative indexing
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# range of indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# example
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# example
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# Range of Negative Indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# example
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# change item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# change a range of item Value
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# insert new value 
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# insert less items than replace
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# insert() without replacing
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# add item at the end of the list
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# insert items at specified Index
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# append elements from another list to the current list
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# add other iterable object
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# remove
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# removes the first item
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# pop()
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# pop() removes last item
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# del removes Index
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# del deletes the list completely
# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist) error
 
#  clear() empties the list (doesnt dissapear)
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# loop lists

# print all items
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# Through the Index Numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist))
#     print(thislist[i])

# while loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# Looping Using List Comprehension
#   thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# list Comprehension

# example
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# example (short version)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# condition
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if x != "apple"]

# print(newlist)

# example
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits]
# print(newlist)

# create an iterable

# newlist = [x for x in range(10)]
# print(newlist)

# outputs [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# with condition

# newlist = [x for x in range(10) if x < 5]

# print(newlist)
# outputs  
# [0, 1, 2, 3, 4]

# expression (before for)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)\
# outputs ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# example

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)
# outputs ['hello', 'hello', 'hello', 'hello', 'hello']


# expression with condition

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)
# outputs ['apple', 'orange', 'cherry', 'kiwi', 'mango']


# sort()

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# outputs ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# sort numerically

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# sort in descending order

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# example

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# sorting by difference between numbers

# def myfunc(n):
#       return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# case sensitive - sorting by capital letters (they will be first)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# case-insensitive (sorting by lower letters)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# reverse regardless of a alphabet
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# copy

# example

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# 2nd method of copy

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# join 

# example

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# 2nd method with append (add to the end)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

# 3rd method with extend (add elements from one list to another list)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)


# list methods

# count() (Return the number of times the value "cherry" appears in the fruits list:)

# fruits = ['apple', 'banana', 'cherry']
# x = fruits.count("cherry")
# print(x)

# example

# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# x = points.count(9)
# print(x)


# exercise1

# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

# exercise2

# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"

# exercise3

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")

# exercise4

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1, "lemon")

# exercise5

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")

# exercise6

# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

# exercise7

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])

# exercise8

# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))




# TUPLE

# example

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)


# allow duplicate values

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)


# length

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# one item tuple

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple    string
# thistuple = ("apple")
# print(type(thistuple))


# data types

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# print(tuple1)
# print(tuple2)
# print(tuple3)


# various data types tuple

# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)


# type

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))


# make tuple

# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)


# access 

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# negative indexing

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])


# range of Indexes

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# example

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])


# range of negative Indexes

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# check if item exists

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")


# change tuple values (convert tuple to list and again)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)


# add element to tuple

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)


# add tuple to tuple

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


# remove items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)


# del tuple (delete tuple completely)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists



# packing tuple

# fruits = ("apple", "banana", "cherry")
# print(fruits)


# unpacking tuple

# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# apple
# banana
# cherry


# asterisk (If the number of variables is less than the number of values, it will be as a list)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# apple
# banana
# ['cherry', 'strawberry', 'raspberry']


# example

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)


# apple
# ['mango', 'papaya', 'pineapple']
# cherry



# loop through a tuple

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


# loop through the index numbers

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# while loop

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1


# join tuples

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# multiply tuples

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


# tuple count method

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# print(x)

# 2


# exercise1

# fruits = ("apple", "banana", "cherry")
# print(fruits[0])

# exercise2

# fruits = ("apple", "banana", "cherry")
# print(len(fruits))

# exercise3

# fruits = ("apple", "banana", "cherry")
# print(fruits[-1])

# exercise4

# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[2:5])



# SETS


# thisset = {"apple", "banana", "cherry"}
# print(thisset)


# duplicated are not allowed

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)


# example (true = 1 same value)

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)


#false (false = 0 same value)

# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)

# length

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))


# data types

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# print(set1)
# print(set2)
# print(set3)


# example

# set1 = {"abc", 34, True, 40, "male"}
# print(set1)


# what type

# myset = {"apple", "banana", "cherry"}
# print(type(myset))


# makeset

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)


# access set

# loop througth the set

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# example

# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)


# add items to the set

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)


# add items from another set

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)


# add any iterable

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# {'banana', 'cherry', 'apple', 'orange', 'kiwi'}


# remove item

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)    

# if the element doesnt exist, remove will give an error


# another method to remove

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# discard doesnt give error


# remove random item

# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)


# clear

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# output set()


# delete the set

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)


# loop items

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)


# join two sets

# union returns a new set with all items from both sets:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# outputs {'c', 3, 'a', 2, 'b', 1}


# update() method inserts the items in set2 into set1:

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)

# outputs {1, 2, 3, 'a', 'c', 'b'}


# both exclude duplucates


# keep only duplicates

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)

# {'apple'}


# new set with duplicates

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)
# {'apple'}


# Keep All, But NOT the Duplicates

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# {'google', 'banana', 'microsoft', 'cherry'}


# new set with unique set

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)

# {'google', 'banana', 'microsoft', 'cherry'}


# example

# x = {"apple", "banana", "cherry", True}
# y = {"google", 1, "apple", 2}

# z = x.symmetric_difference(y)

# print(z)

# {2, 'google', 'cherry', 'banana'}


# difference - set that contains the items that only exist in set x, and not in set y

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.difference(y) 

# print(z)

# {'cherry', 'banana'}


# returns an item that in both sets

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.difference_update(y) 

# print(x)

# {'cherry', 'banana'}


# exercise1

# fruits = {"apple", "banana", "cherry"}
# if "apple" in fruits:
#     print("Yes, apple is a fruit!")

# exercise2

# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")

# exercise3

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)

# exercise4

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")

# exercise5

# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")



# DICTIONARY

# thedict = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964
# }
# print(thedict)

# output {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# example

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])


# duplicates will overwrite

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)


# length

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(len(thisdict))

# output: 3

# data types

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict)


# type

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))


# make a dict

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict) 

# outputs {'name': 'John', 'age': 36, 'country': 'Norway'}


# access items

# example

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)


# 2nd method

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)


# returns keys

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.keys()
# print(x)

# dict_keys(['brand', 'model', 'year'])


# add new item

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# output:
# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])


# return values

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.values()

# print(x)

# output dict_values(['Ford', 'Mustang', 1964])


# change the Value

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# output:
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])


# adding new item, change dict_values

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# output:
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 1964, 'red'])


# return each item as tuples in a list

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.items()

# print(x)

# output : dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# example

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change


# example

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# change dict_values

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict["year"] = 2018

# print(thisdict)

# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# 2nd way

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# print(thisdict)

# adding items

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)


# adding using update

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})


# remove items

# pop - removes key

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# {'brand': 'Ford', 'year': 1964}

# popitem() - removes the last inserted item (in versions before 3.7, a random item is removed instead):

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}


# del 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# del deletes completely

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# clear

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# {}


# loops throught dict
 
#  example

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)

# brand
# model
# year

# example

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])

# Ford
# Mustang
# 1964


# to return dict_values

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)


# to return dict_keys

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)


# to return both

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)

# brand Ford
# model Mustang
# year 1964


# copy 


# copy() 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)


# dict()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# nested dictionaries

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)

# {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


# add three dict into new 

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)
# {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}


# access

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child2"]["name"])


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child2"]["name"])
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child2"]["name"])

# Tobias


# exercise1

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))

# exercise2

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["year"] = 2020

# exercise3

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red"

# exercise4

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.pop("model")

# exercise5

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()




# IF...else

# if statement

# a = 33
# b = 200

# if b > a:
#   print("b is greater than a")


#  IndentationError

# a = 33
# b = 200

# if b > a:
# print("b is greater than a")


# elif (else) - "if the previous conditions were not true, then try this condition".

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# else ( catches anything which isn't caught by the preceding conditions)
      
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# example

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


# short hand if

# a = 200
# b = 33

# if a > b: print("a is greater than b")


# short hanf if else

# a = 2
# b = 330

# print("A") if a > b else print("B")


# multiple else statements

# a = 330
# b = 330

# print("A") if a > b else print("=") if a == b else print("B")


# and

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")


# or

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")


# not

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")


# nested if (if inside if)

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# Above ten,
# and also above 20!


# pass (if statements cannot be empty, but if you for some reason have an if statement with no content)

# a = 33
# b = 200

# if b > a:
#   pass

# having an empty if statement like this, would raise an error without the pass statement


# exercise1

# a = 50
# b = 10
# if a > b:
#    print("Hello World")

# exercise2

# a = 50
# b = 10
# if a != b:
#    print("Hello World")

# exercise3

# a = 50
# b = 10
# if a == b:
#    print("Yes")
# else:
#    print("No")

# exercise4

# a = 50
# b = 10
# if a == b:
#    print("1")
# elif a > b:
#    print("2")
# else:
#    print("3")


# exercise5

# if a == b and c == d:
#    print("Hello")

# exercise6

# if a == b or c == d:
#     print("Hello")

# exercise7

# if 5 > 2:
#     print("YES")

# exercise8

# a = 2
# b = 5
# print("YES") if a == b else print("NO")

# exercise9

# a = 2
# b = 50
# c = 2

# if a == c or b == c:
#    print("YES")



# WHILE loops

# example

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# 1
# 2
# 3
# 4
# 5


# break

# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1


# continue

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# # Note that number 3 is missing in the result


# else
  
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6


# exercise1

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# exercise2

# i = 1
# while i < 6:
#   if i == 3:
#     break
#   i += 1

# exercise3

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#         continue
#   print(i)

# exercise4

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#     print("i is no longer less than 6")




# FOR loops

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 


# looping through a string

# for x in "banana":
#       print(x) 

# b
# a
# n
# a
# n
# a


# break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break

# apple
# banana


# example

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x) 

# apple


# continue

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x) 

# apple
# Cherry


# range

# for x in range(6):
#       print(x) 


# for x in range(6):
#   print(x) 

# for x in range(6):
#   print(x) 
# ​
# 0
# 1
# 2
# 3
# 4
# 5

# example

# for x in range(2, 6):
#       print(x)

# 2
# 3
# 4
# 5

# example

# for x in range(2, 30, 3):
#       print(x) 

# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

# else

# for x in range(6):
#       print(x)
# else:
#   print("Finally finished!")

# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

# example

# for x in range(6):
#       if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# #If the loop breaks, the else block is not executed.


# nested loops

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# pass

# for x in [0, 1, 2]:
#       pass

# # having an empty for loop like this, would raise an error without the pass statement




# exercise1

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#    print(x)

# exercise2

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# exercise3

# for x in range(6):
#    print(x)

# exercise4

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)