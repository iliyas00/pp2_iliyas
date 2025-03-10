#  задание
#  напишите сортировку с лямбдой, которая вернёт минимальный элемент из списка `people`, сортировка должна быть
#  сначала по возрасту, а потом по имени


people = [
    {"name": "Alice", "age": 26},
    {"name": "Charlie", "age": 23},
    {"name": "Bob", "age": 21},
    {"name": "Diana", "age": 30},
]

min_people = min(people, key=lambda element: (element["age"], element["name"]))
print(min_people)

max_peeople = max(people, key=lambda element: (element["age"], element["name"]))
print(max_peeople)

min_age_people = min(people, key=lambda element: element["name"])
print(min_age_people)