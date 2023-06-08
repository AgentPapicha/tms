import json
import csv

# Открываем JSON файл и загружаем данные
with open('data.json', 'r') as f:
    data = json.load(f)

# Открываем CSV файл для записи
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Записываем заголовки столбцов
    writer.writerow(['Имя', 'Фамилия', 'Email', 'Телефон'])

    # Записываем данные из JSON файла в CSV файл
    for item in data:
        writer.writerow([item['name'], item['surname'], item['email'], item['phone']])