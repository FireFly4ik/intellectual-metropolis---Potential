#Используемый язык - Python 3.9

a = []
with open("history_mirror.txt", "r", encoding="utf-8") as file: #открывается файл для занесения в массив
    q = file.readline()
    for row in file.readlines():
        a.append(row.replace("\n", "").split("="))

#поиск людей с ошибкой
with open("answers/1/mirror_error.txt", "w", encoding="utf-8") as file:
    for x in a:
        if x[2] == "error":
            file.write(f"У пользователя <{x[1].split()[0]} {x[1].split()[1][0]}.{x[1].split()[2][0]}> <{x[0]}> появилась ошибкая\n")
            last = f"Ошибка была зафиксирована: <{x[0]}> у пользователя <{x[1].split()[0]} {x[1].split()[1][0]}.{x[1].split()[2][0]}>"

print(last)