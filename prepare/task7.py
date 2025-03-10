#sort_by_lambda = lambda person: len(person)

#print(sort_by_lambda("ilyas"))

fruits = ["banana", "apple", "cherry", "date"]

#sort_fruits = sorted(fruits, reverse=True)
#print(sort_fruits)



#def sort_by_len(element):
#    return len(element)

#sort_fruits = sorted(fruits, key=sort_by_len)
#print(sort_fruits)


#sort_fruits = sorted(fruits, key=lambda element: len(element))
#print(sort_fruits)


longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)