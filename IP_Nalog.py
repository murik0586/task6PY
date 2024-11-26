"""
Программу - помощник ИП, ему выбрать лучшую систему налогообложения.


Пример
Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
1 <Enter>
Введите сумму дохода:
400 <Enter>

Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
2 <Enter>
Введите сумму расхода:
100 <Enter>

Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
1 <Enter>
Введите сумму дохода:
600 <Enter>

Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
3 <Enter>

Мы советуем вам УСН доходы
Ваш налог составит: 60 рублей
Налог на другой системе: 135 рублей
Экономия: 75 рублей

Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
end <Enter>

"""


text_operation = '''Выберите операцию и введите её номер:
1. Добавить новый доход
2. Добавить новый расход
3. Выбрать систему налогообложения
4. Или введите "end" для выхода\n'''

earning = 0
spending = 0


def tax_earnings_minus_spending(earnings: int, spendings: int) -> int:
    tax = (earnings - spendings) * 15 / 100
    if tax >= 0: return int(tax)  # Это специально выбрано, чтобы не было float. Так задумано
    return 0


def tax_usn(earnings: int) -> int:
    return int(earnings * 6 / 100)


while True:

    operation = input(text_operation)
    if operation == "end": print("Программа завершена"); break
    menu = int(operation)
    total_earn_minus_spent = tax_earnings_minus_spending(earning, spending)
    total_earn = tax_usn(earning)
    match menu:
        case 1:
            earning += int(input("Введите доход, босс!\n"))
        case 2:
            spending += int(input("Введите расход, босс!\n"))
        case 3:
            if total_earn_minus_spent > total_earn:
                print(f"""Мы советуем вам УСН доходы
Ваш налог составит: {total_earn} рублей
Налог на другой системе: {total_earn_minus_spent} рублей
Экономия: {total_earn_minus_spent - total_earn}""")
            else:
                print(f"""Мы советуем вам УСН доходы-минус расходы
Ваш налог составит: {total_earn_minus_spent} рублей
Налог на другой системе: {total_earn} рублей
Экономия: {total_earn - total_earn_minus_spent}""")
