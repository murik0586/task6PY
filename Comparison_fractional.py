from math import trunc

text_menu = """Операции над float
1. Сравнить
2. Округлить
3. Отбросить дробную часть
0. Выход
"""

while True:
    operation_float = int(input(text_menu))

    match operation_float:
        case 1:
            one_number, two_number = float(input("Введите первое число \n")), float(input("Введите второе число\n"))
            if one_number == two_number:
                print("Числа равны!")
            else:
                print("Числа не равны!")
        case 2:
            one_number = float(input("Введите число для округления!\n"))

            print(f"Результат округления: {round(one_number)}")
        case 3:
            one_number = float(input("Введите число для отброса дробной части\n"))
            print(f"{trunc(one_number)}")