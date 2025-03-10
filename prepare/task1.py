number = input()

number = number.split()

if len(number) == 3:
    num1, op, num2 = number
    
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)

        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("Na nol nelzya!")
            else:
                print(num1 / num2)
        else:
            print("Wrong format")
    else:
        print("Wrong format")
else:
    print("Wrong format")