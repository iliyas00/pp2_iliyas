# CLASSES

# Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

# class my_class:
#     def getString(self):
#         a = str(input())
#         return a
#     def printString(self, c):
#         print(c.upper())
# p1 = my_class()
# b = p1.getString()
# p1.printString(b)


# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def area(self, a = 0):
#         print(a)
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         print(self.length * self.length)
# p1 = Shape()#p1 is an object of class
# p2 = Square(2)#p2 is an object of a subclass
# p1.area()
# p2.area()


# Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# class Shape:
#     def area(self, a = 0):
#         print(a)
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print(self.length * self.width)
# p1 = Rectangle(4, 5)#p1 is an object of a Rectangle subclass
# p2 = Shape()#p2 is an object of a class Shape
# p1.area()
# p2.area()


# Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"({self.x},{self.y})")
#     def move(self):
#         self.x = int(input("new x coordinate: "))
#         self.y = int(input("new y coordinate: "))
#     def dist(self, obj):
#         print ((((obj.x - self.x)**2) + ((obj.y - self.y)**2))**0.5)
# p1 = Point(2, 4)#added point 1
# p2 = Point(5, 6)#added point 2
# p1.show()#see the coordinates of point 1
# p1.move()#change the coordinates of point 1
# p1.show()#see how the coordinates of point 1 have changed
# p2.show()#see the coordinates of point 2
# p1.dist(p2)#see the distance between point 1 and point 2


# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

# class bank_account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, d):
#         self.balance += d
#     def withdraw(self, w):
#         if w > self.balance:
#             print("withdrawals may not exceed the available balance")
#         else:
#             self.balance -= w
#     def __str__(self):
#         return (f"{self.owner}, {self.balance}")
# p1 = bank_account("Dilnaz", 10000)
# print(p1)
# p1.deposit(10000)
# print(p1)
# p1.withdraw(5000)
# print(p1)
# p1.withdraw(10000)
# print(p1)


# Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

# class isPrime:
#     def __init__(self, numbers):
#         self.numbers = numbers

#     def is_prime(self, num):
#         if num < 2:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True

#     def filter_prime(self):
#         return filter(lambda x: self.is_prime(x), self.numbers)

# numbers = [1, 3, 4, 5, 2, 34, 7, 6]
# p1 = isPrime(numbers)
# p2 = p1.filter_prime()
# print("Prime numbers in the list:", list(p2))



# FUNCTION1

# A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

# a = float(input())

# def func(b):
#     return 28.3495231 * b
# print(func(a))


# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)


# F = float(input())#read in Fahrenheit
# def my_function(f):
#     return (5/9) * (f - 32)
# print(my_function(F))


# You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def filter_prime(numbers):
#     prime_numbers = []
#     for num in numbers:
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers

# numbers = [1, 3, 4, 5, 2, 34, 7, 6]
# print("Prime numbers in the list:", filter_prime(numbers))


# Write a function that accepts string from user and print all permutations of that string.

# from itertools import permutations

# def generate_permutations(string):
#     chars = list(string)  # Convert the string to a list of characters
#     perms = permutations(chars) # Generate permutations using itertools
#     for perm in perms:
#         print(''.join(perm))

# user_input = input()
# generate_permutations(user_input)


# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

# def toReverse(s):
#     reversed_s = " ".join(reversed(s.split()))
#     print(reversed_s)
# s = str(input())
# toReverse(s)


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# def has_33(nums):
#     pass

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# a = [1, 1, 3, 3]#function must return true
# b = [1, 3, 2, 1, 3]#function must return false
# def has_33(num):
#     ft = False
#     i = 0
#     while i != len(num):
#         if ft == False:
#             if num[i] == 3:
#                 ft = True
#         else:
#             if num[i] == 3:
#                 return True
#             else:
#                 ft = False
#         i += 1
#     return False
# print(has_33(a))
# print(has_33(b))


# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False


# def spy_game(nums):
#     pos_0 = False  #for position of two zeros
#     pos_1 = False

#     for num in nums:
#         if num == 0 and not pos_0 and not pos_1: # if current number is 0, and both pos_0 and pos_1 are False, set pos_0 to True
#             pos_0 = True
#         elif num == 0 and pos_0 and not pos_1: # if current number is 0, and pos_0 is True but pos_1 is False, set pos_1 to True
#             pos_1 = True
#         elif num == 7 and pos_0 and pos_1: # if current number is 7, and both pos_0 and pos_1 are True, return True
#             return True

#     return False

# print(spy_game([1,2,4,0,0,7,5]))  # True
# print(spy_game([1,0,2,4,0,5,7]))  # True
# print(spy_game([1,7,2,0,4,5,0]))  # False


# Write a function that computes the volume of a sphere given its radius.

# import math

# def volumeOfSphere(radius):
#     return (4/3) * math.pi * pow(radius, 3)

# radius = int(input())
# Volume = volumeOfSphere(radius)
# print(Volume)


# Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

# def unique(input_list):
#     unique_list = []
#     for i in list1:
#         if i not in unique_list:
#             unique_list.append(i)

#     return unique_list

# list1 = input().split()
# print(unique(list1))


# Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

# def isPalindrome(word):
#     reversed_word = ""
#     for char in reversed(word):
#         reversed_word += char
#     if reversed_word == word:
#         print("is palindrome")
#     else:
#         print("not palindrome")

# my_string = input()
# isPalindrome(my_string)


# Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

# def histogram(inputList):
#     for i in inputList:
#         print("*" * i)

# myList = [5, 10, 9]
# histogram(myList) 



# FUNCTION2

# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# 1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5

# def imdb(movie):
#     for i in movies:
#         if i["name"] == movie:
#             if i["imdb"] >= 5.5:
#                 return True
#     return False


# 2 Write a function that returns a sublist of movies with an IMDB score above 5.5.

# mylist = []
# def checking():
#     for i in movies:
#         if i["imdb"] >= 5.5:
#             mylist.append(i["name"])
#     return mylist

# 3 Write a function that takes a category name and returns just those movies under that category.

# mylist = []
# def checking(category_name):
#     for i in movies:
#         if(i["category"] == category_name):
#             mylist.append(i["name"])
#     return mylist

# print(checking("Romance"))


# 4 Write a function that takes a list of movies and computes the average IMDB score.

# def avgIMDB():
#     sumOfIMDB = 0
#     for i in movies:
#         sumOfIMDB += i["imdb"]
#     return sumOfIMDB / len(movies)

# 5 Write a function that takes a category and computes the average IMDB score.

# def checking(category_name):
#     sumOfIMDB = 0
#     cnt = 0
#     for i in movies:
#         if(i["category"] == category_name):
#             cnt += 1
#             sumOfIMDB += i["imdb"]
#     return sumOfIMDB / cnt