#Используемый язык - Python 3.9

a = []
with open("answers/history_mirror.txt", "r", encoding="utf-8") as file: #открывается файл для занесения в двумерный массив
    q = file.readline()
    for row in file.readlines():
        a.append(row.replace("\n", "").replace("-", "").split("="))

b = {} #создание словаря запросов
for row in a: #добавление в словарь количества запросов
    if row[2] not in b:
        b[row[2]] = 1
    else: b[row[2]] += 1

b = sorted(b.items(), key=lambda item: item[1], reverse=True) #сортивока запросов
for i in range(5): #вывод 5 поплуярных запросов
    print(f'<{b[i][0]}> - <{b[i][1]}>')