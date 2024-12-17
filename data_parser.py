import csv


def load_csv(file_path):

    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as file:  # utf-8-sig убирает BOM
            reader = csv.DictReader(file)
            for row in reader:
                # Очистка ключей от невидимых символов (например, BOM)
                cleaned_row = {key.strip(): value for key, value in row.items()}
                data.append(cleaned_row)
        print("Заголовки столбцов:", list(data[0].keys()))  # Для отладки ключей
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
    return data


def transform_data(client):

    fio = client['name']  # Было 'ФИО', теперь 'name'
    gender = "женского" if client['sex'].lower() == "female" else "мужского"
    age = client['age']
    amount = client['bill']
    device = client['device_type']
    browser = client['browser']
    region = client['region']

    # Формируем текст по шаблону
    return (f"Пользователь {fio} {gender} пола, {age} лет совершил(а) покупку на {amount} у.е. "
            f"с {device} браузера {browser}. Регион, из которого совершалась покупка: {region}.")


def write_to_txt(output_file, descriptions):

    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            for desc in descriptions:
                file.write(desc + "\n")
        print(f"Данные успешно записаны в {output_file}")
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")


def main():

    input_file = "web_clients_correct.csv"  # Файл с исходными данными
    output_file = "clients_descriptions.txt"  # Файл для записи описаний

    # Шаг 1: Загрузка данных
    clients_data = load_csv(input_file)
    if not clients_data:
        print("Нет данных для обработки.")
        return

    # Шаг 2-3: Преобразование данных и формирование описаний
    descriptions = [transform_data(client) for client in clients_data]

    # Шаг 4: Запись данных в текстовый файл
    write_to_txt(output_file, descriptions)


if __name__ == "__main__":
    main()