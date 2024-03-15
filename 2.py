#Используемый язык - Python 3.9

a = []
with open("answers/history_mirror.txt", "r", encoding="utf-8") as file: #открывается файл для занесения в двумерный массив
    q = file.readline()
    for row in file.readlines():
        a.append(row.replace("\n", "").replace("-", "").split("="))

#пузырьковая сортировка
tempa = []
while (tempa != a):
    tempa = a.copy()
    for x in range(len(a) - 1):
        if a[x][0] > a[x + 1][0]:
            temp = a[x]
            a[x] = a[x + 1]
            a[x + 1] = temp

#вывод 5 самых первых событий
for i in range(5):
    print(f"<{a[i][0][:4]}-{a[i][0][4:6]}-{a[i][0][6:]}> - <{a[i][1]}> - <{a[i][2]}>")