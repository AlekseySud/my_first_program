operation = input("Введите операцию(+,-,*,/, стоп - закончить): ")
while operation != 'стоп':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = 0
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if a == 0:
            print("На 0 делить нельзя")
            exit()
        result = a / b
    else:
        print("Неизвестная операция")

    print(result)
    operation = input("Введите операцию(+,-,*,/, стоп - закончить): ")