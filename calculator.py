oper = ['+', '-', '*', '/']

name = input("Введите имя: ")
print(f"Привет {name}!")

while True:


    while True:
        operator = input("Выбери оператор: ('+' ,'-' ,'*', '/'):  ")
        if operator in oper:
            break
        print("Неверный оператор: Введите оператор! ('+' ,'-' ,'*', '/')")
            
    try:

        num_one = int(input("Первое число: "))
        num_two = int(input("Второе число: "))
    except ValueError:
        print("Ошибка: Нужно ввести число!")
        continue


    try:

        if operator == '+':
            print(num_one + num_two)
        elif operator == '-':
            print(num_one - num_two)
        if operator == '*':
            print(num_one * num_two)
        elif operator == '/':
            print(num_one / num_two)

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль нельзя!")
        continue

    answer = input("Хотите продолжить?: (да/нет) ")
    if answer == 'нет':
        break

