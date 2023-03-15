def calcule():
    num1 = int(input("Choose a number: "))
    operator = input("Choose an operator: ")
    num2 = int(input("Choose a number: "))
    
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "%":
        print(num1%num2)
    else:
        print("ERROR")
    print(num1,"",operator,"",num2)
calcule()