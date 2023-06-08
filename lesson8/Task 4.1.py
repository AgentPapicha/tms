import json
import csv

# Открываем JSON файл и загружаем данные
with open('data_file.json', 'r') as f:
    data = json.load(f)
print(data)
# Открываем CSV файл для записи
with open('data_file.json', 'r') as json_file, open('data.csv', 'w', newline='') as csv_file:
    # Загружаем данные из json файла
    data = json.load(json_file)

    # Создаем объект writer для записи в csv файл
    writer = csv.writer(csv_file)

    # Записываем заголовки столбцов
    writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])

    # Записываем данные из json файла в csv файл
    for id, info in data.items():
        writer.writerow([id, info[0], info[1], ''])

print('Данные успешно записаны в файл data.csv')
