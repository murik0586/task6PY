price_list: list = []
while True:
    menu = input("""
1.Ввести магазин, товар и цену
2.Вывести результат
Для выхода введите 'Выход'
""")
    if menu == 'Выход': break
    if menu.isdigit():
        menu = int(menu)
        match menu:
            case 1:
                print("Для возвращения назад введите 'назад'")

                shop = input("Введите название магазина\n")
                if shop.lower() == "назад": break
                product = input("Введите название продукта\n") ## может стоит сделать списком
                if product.lower() == "назад": break
                price = input("Введите цену\n")
                if price.lower() == "назад": break
                else: int(price)

                shops_and_price = {"Магазин ": shop, "Товар ": product, "Цена ": price}
                price_list.append(shops_and_price)
                print("Успешно добавили!")
            case 2: ##TODO Затем программа должна вывести список магазинов и общую стоимость покупок в каждом магазине, а также сообщить, в каком магазине пользователь может сэкономить больше всего денег.
                print(price_list)
