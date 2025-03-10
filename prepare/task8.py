squares = []

for x in range(1, 10):
    squares.append(x ** 2)
    

print(squares) 
squares = [x ** 2 for x in range(1, 10, 2)]
print(squares)