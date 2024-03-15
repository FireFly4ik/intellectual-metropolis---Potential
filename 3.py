#Используемый язык - Python 3.9

a = []
with open("answers/history_mirror.txt", "r", encoding="utf-8") as file: #открывается файл для занесения в двумерный массив
    q = file.readline()
    for row in file.readlines():
        a.append(row.replace("\n", "").replace("-", "").split("="))

#проверка ввода человека
q = input()
while q != "mirror":
    for row in a:
        if row[1].split()[0] == q:
            print(f"Предсказание для <{row[1].split()[0]} {row[1].split()[1][0]}.{row[1].split()[2][0]}> - <{row[2]}>")
    q = input()