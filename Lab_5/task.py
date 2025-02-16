# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
# Напишите программу на Python, которая соответствует строке, содержащей букву "a", за которой следует ноль или более букв "b".

# import re

# pattern = r'a*b*'
# input_string = 'aabbbb'

# match = re.match(pattern, input_string)

# if match:
#     print("Match found!")
# else:
#     print("No match found.")


#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# import re

# string = input('Enter a string: ')

# pattern = r'ab{2,3}'

# if re.search(pattern, string):
#     print("Match found!")
# else:
#     print('Match not found.')


# 3. Write a Python program to find sequences of lowercase letters joined with a underscore.
# Напишите программу на Python для поиска последовательностей строчных букв, соединенных символом подчеркивания.

# import re

# text = input('Enter string: ').split(",")
# pattern = r"[a-z][_]"

# for i in text:
#     if re.search(pattern, i):
#         print(i)



# 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# import re

# text = input('Enter a string: ').strip() #strip removes white spaces
# pattern = r"[A-Z][a-z]+" #+ one or more
# matches = re.findall(pattern, text)
# print(matches)



# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
#Напишите программу на Python, которая соответствует строке с буквой "a", за которой следует что угодно, заканчивающееся на "b"

# import re
# text = input("Enter a string: ")
# pattern = r'a.*b$' #.* matches zero or more of any character (except for newline).
#                 #b$ matches the character 'b' at the end of the string 
# match = re.match(pattern, text) 

# if match:
#     print("Match found!")
# else:
#     print("No match found.")



# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# text = input("Enter a string: ")
# result = text.replace(' ', ':').replace(',', ':').replace('.', ':')

# print("Result:", result)



# 7. Write a python program to convert snake case string to camel case string.
# snake case - my_variable
# camel case - MyVariable

# snake_case = "hello_world_how_are_you"

# camel_case = snake_case.title().replace("_", "")  #Title case capitalizes the first letter of each word and converts the rest of the word to lowercase. 

# print(camel_case)


# 8. Write a Python program to split a string at uppercase letters.

# import re

# text = "SplitThisStringAtUppercaseLetters"

# split_text = re.findall('[A-Z][^A-Z]*', text)

# print(split_text) 


# 9. Write a Python program to insert spaces between words starting with capital letters.
# Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.

# import re

# text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

# new_text = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

# print(new_text) 


# 10. Write a Python program to convert a given camel case string to snake case.

# def camel_to_snake(camel_str):
#     snake_str = ''
#     for i, char in enumerate(camel_str):
#         if i > 0 and char.isupper():
#             snake_str += '_'
#         snake_str += char.lower()
#     return snake_str


# camel_str = "CamelCaseString"
# snake_str = camel_to_snake(camel_str)
# print(snake_str)



# import re

# def parse_receipt(text):
#     match = re.search(r'Филиал (.+)\n', text)
#     branch = match.group(1) if match else None

#     match = re.search(r'БИН (\d+)\n', text)
#     bin_number = match.group(1) if match else None

#     match = re.search(r'Чек №(\d+)\n', text)
#     check_number = match.group(1) if match else None

#     match = re.search(r'Касса (.+)\n', text)
#     cash_register = match.group(1) if match else None

#     match = re.search(r'Смена (\d+)\n', text)
#     shift = match.group(1) if match else None

#     match = re.search(r'ПРОДАЖА\n((?:.+\n)+)', text)
#     sales_items = match.group(1) if match else None

#     match = re.search(r'ИТОГО:\n([\d\s,]+)', text)
#     total = match.group(1).replace(" ", "") if match else None
#     return {
#         "branch": branch,
#         "bin_number": bin_number,
#         "check_number": check_number,
#         "cash_register": cash_register,
#         "shift": shift,
#         "sales_items": sales_items,
#         "total": total
#     }
# with open('row.txt', 'r', encoding='utf-8') as file:
#     receipt_text = file.read()

# parsed_receipt = parse_receipt(receipt_text)
# for key, value in parsed_receipt.items():
#     print(f"{key}: {value}")