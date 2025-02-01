# #string
# print("Hello")
# print('Hello')

# #example
# a = "Hello"
# print(a)

# #example
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# #example
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# #example
# a = "Hello, World!"
# print(a[1])

# #example
# for x in "banana":
#       print(x)

# #example
# a = "Hello, World!"
# print(len(a))

# #example
# txt = "The best things in life are free!"
# print("free" in txt)

# #example
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# #example
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# #example
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")


# #slicing
# b = "Hello, World!"
# print(b[2:5])

# #slice from the start
# b = "Hello, World!"
# print(b[:5])

# #slice to the end
# b = "Hello, World!"
# print(b[2:])

# #negative indexing
# b = "Hello, World!"
# print(b[-5:-2])


# #uppercase
# a = "Hello, World!"
# print(a.upper())

# #lowercase
# a = "Hello, World!"
# print(a.lower())

# #remove whitespace
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"

# #replace string
# a = "Hello, World!"
# print(a.replace("H", "J"))

# #split string
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# #string concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# #example
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# #format strings
# #error
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# #insert numbers into strings
# age = 36
# txt = "My name is John, I am {}"
# print(txt.format(age))

# #example
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# #example
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


# #error 
# txt = "We are the so-called "Vikings" from the north."

# #example
# txt = "We are the so-called \"Vikings\" from the north."

# #single quote
# txt = 'It\'s alright.'
# print(txt) 

# #backslash
# txt = "This will insert one \\ (backslash)."
# print(txt) 

# #newline
# txt = "Hello\nWorld!"
# print(txt) 

# #carriage retern
# txt = "Hello\rWorld!"
# print(txt) 

# #tab
# txt = "Hello\tWorld!"
# print(txt) 


# #This example erases one character (backspace):
# txt = "Hello \bWorld!"
# print(txt) 

# #octal value
# txt = "\110\145\154\154\157"
# print(txt) 

# #hex
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 

# #exercise1
# x = "Hello World"
# print(len(x))

# #exercise2
# txt = "Hello World"
# x = txt[0]

# #exercise3
# txt = "Hello World"
# x = txt[2:5]

# #exercise4
# txt = " Hello World "
# x = txt.strip()

# #exercise5
# txt = "Hello World"
# txt = txt.upper()

# #exercise6
# txt = "Hello World"
# txt =  txt.lower()

# #exercise7
# txt = "Hello World"
# txt = txt.
# replace("H", "J")

# #exercise8
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))