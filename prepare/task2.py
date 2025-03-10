
table = input()
answer = 0

t_table = table.split()

for i in range(len(t_table)):
    if t_table[i] == "+":
        answer = int(t_table[i - 1]) + int(t_table[i + 1])
    elif t_table[i] == "-":
        answer = int(t_table[i - 1]) - int(t_table[i + 1])
    elif t_table[i] == "*":
        answer = int(t_table[i - 1]) * int(t_table[i + 1])
    elif t_table[i] == "/":
        answer = int(t_table[i - 1]) / int(t_table[i + 1])
    
print(answer)