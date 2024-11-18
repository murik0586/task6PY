import csv
import json

# Путь к файлам
visit_log_file = 'visit_log__1___2_.csv'
purchase_log_file = 'purchase_log.txt'
funnel_file = 'funnel.csv'

# Считываем данные о покупках из файла purchase_log.txt
purchase_dict = {}
with open(purchase_log_file, 'r', encoding='utf-8') as f:
    for line in f:
        purchase_data = json.loads(line.strip())  # Преобразуем строку JSON в словарь
        user_id = purchase_data["user_id"]
        category = purchase_data["category"]
        purchase_dict[user_id] = category  # Сохраняем категорию для каждого пользователя

# Открываем файл для записи данных с визитами и категориями покупок
with open(funnel_file, 'w', newline='', encoding='utf-8') as fout:
    writer = csv.writer(fout)
    # Записываем заголовок
    writer.writerow(['user_id', 'source', 'category'])

    # Считываем данные о визитах из файла visit_log__1___2_.csv
    with open(visit_log_file, 'r', encoding='utf-8') as fin:
        reader = csv.reader(fin)
        # Пропускаем заголовок
        next(reader)

        # Обрабатываем строки визитов
        for row in reader:
            user_id = row[0]  # user_id из визита
            source = row[1]  # Источник визита

            # Если для данного user_id есть покупка, добавляем категорию в файл
            if user_id in purchase_dict:
                category = purchase_dict[user_id]  # Получаем категорию покупки
                # Записываем информацию в файл
                writer.writerow([user_id, source, category])

print("Файл funnel.csv успешно создан.")