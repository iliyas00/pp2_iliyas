# DATE

# 1. Write a Python program to subtract five days from current date.

# from datetime import datetime, timedelta
# current_date = datetime.now() #current date
# new_date = current_date - timedelta(days=5) # Subtract five days
# print("Current date:", current_date.strftime("%Y-%m-%d"))    #year 4 digits, month and day in 2 digits
# print("Date five days ago:", new_date.strftime("%Y-%m-%d"))  #strftime converts datetime to string


# 2. Write a Python program to print yesterday, today, tomorrow.

# from datetime import datetime, timedelta

# current_date = datetime.now()
# yesterday = current_date - timedelta(days=1)
# tomorrow = current_date + timedelta(days=1)

# print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("Today:", current_date.strftime("%Y-%m-%d"))
# print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


# 3. Write a Python program to drop microseconds from datetime.

# from datetime import datetime
# current_datetime = datetime.now()
# without_microseconds = current_datetime.replace(microsecond=0)

# print("Datetime without microseconds:", without_microseconds)


# 4. Write a Python program to calculate two date difference in seconds

# from datetime import datetime
# date1 = datetime(2024, 2, 13, 12, 0, 0)  # Example date 1
# date2 = datetime(2024, 2, 12, 12, 0, 0)  # Example date 2

# difference_in_seconds = abs((date1 - date2).total_seconds())
# print("Difference between the two dates in seconds:", difference_in_seconds)



# GENERATORS

# 1. Create a generator that generates the squares of numbers up to some number N.

# def square_generator(N):
#     for num in range(1, N+1): #N is inclusive
#         yield num * num  #turns the function into a generator, allowing it to produce a series of values one at a time without storing them all in memory.
# N = 5
# squares = square_generator(N)

# for square in squares:
#     print(square)


# 2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

# def even_numbers(n):
#     for num in range(n + 1):
#         if num % 2 == 0:
#             yield num
# n = int(input("Enter a number: "))
# even_nums = even_numbers(n) # Generate even numbers and print them in comma-separated form
# for num in even_nums:
#      print(num, end=',')  #The end=',' tells what to print at the end of each call to print().


# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

# def divisible_by_3_and_4(n):
#     for num in range(n + 1):
#         if num % 3 == 0 and num % 4 == 0:
#             yield num
# n = 20
# for num in divisible_by_3_and_4(n):
#     print(num)


# 4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

# def squares(a, b):
#     for num in range(a, b + 1):
#         yield num ** 2

# a = 10
# b = 10
# for square in squares(a, b):
#     print(square)


# 5. Implement a generator that returns all numbers from (n) down to 0.

# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1
# n = 10
# for num in countdown(n):
#     print(num)



# MATH


# 1. Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904                

# import math
# degree = 15
# radian = degree * (math.pi / 180)
# print("Output radian:", radian)


# 2. Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

# height = 5
# base1 = 5
# base2 = 6
# area = 0.5 * (base1 + base2) * height
# print("Area of the trapezoid:", area)

# 3. Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

# import math
# num_sides = int(input("Input number of sides: "))
# side_length = int(input("Input the length of a side: "))
# area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides)) #tan() function in the math module calculates the tangent of an angle in radians. The tangent of an angle is the ratio of the length of the opposite side to the length of the adjacent side in a right triangle.
# print("The area of the polygon is:", round(area,1))


# 4. Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

# base_length = float(input("Length of base: "))
# height = float(input("Height of parallelogram: "))

# area = base_length * height
# print("The area of the parallelogram is:", area)



# JSON

# import json

# with open('sample-data.json') as file:
#     json_data = json.load(file) 
#     print('''
#     Interface Status
#     ================================================================================
#     DN                                                 Description           Speed    MTU  
#     -------------------------------------------------- --------------------  ------  ------
#     ''')
#     imdata = json_data['imdata']
#     for item in imdata:
#         o_item = item['l1PhysIf']
#         attr = o_item['attributes']
#         dn = attr['dn']
#         speed = attr['speed']
#         mtu = attr['mtu']
#         out = ''
#         if len(dn) == 42:
#             out += dn + '                              ' + speed + '   ' + mtu
#         else:
#             out += dn + '                              ' + speed + '   ' + mtu
#             print(out)