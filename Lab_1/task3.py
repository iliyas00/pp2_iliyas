# variables

#example
# x = 5
# y = "John"

# print(x)
# print(y)

# #example
# x = 4
# x = "Sally"
# print(x)

# #example
# x = str(3)   #x will be 3
# y = int(3)   #y will be 3
# x = float(3)  #z will be 3

# #example
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# #example
# x = "John"
# print(x)
# #double quotes are the same as single quotes:
# x = 'John'
# print(x)

# #example
# a = 4
# A = "Sally"
# print(a)
# print(A)
# #A will not overwrite a


# #variable names

# #example
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

# #illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# #camel case
# myVariableName = "John"

# #pascal case
# MyVariableName = "John"

# #snake case
# my_variable_name = "John"


# #assign multiple values

# #example
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# #one value to multiple variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


#output variables

# x = "Python is awesome"
# print(x)

#example
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

#example
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# #example
# x = 5
# y = 10
# print(x + y)

# #error example
# x = 5
# y = "John"
# print(x + y)

# #example
# x = 5
# y = "John"
# print(x, y)


#global variables

#example
# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc()

#example
# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Pythos is " + x)

#global keyword
# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)

#example
# x = "awesome"

# def myfunc():
#     global x
#     x = "fantastic"

# myfunc()

# print("Python is " + x)


#exercise1
# carname = "Volvo"

# #exercise2
# x = 50

# #exercise3
# x = 5
# y = 10
# print(x + y)

# #exercise4
# x = 5
# y = 10
# z = x + y
# print(z)

# #exercise5
# x, y, z = "Orange", "Banana", "Cherry"

# #exercise5
# x=y=z = "Orange"

# #exercise5
# def myfunc():
#     global x
#     x = "fantastic"