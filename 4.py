#Используемый язык - Python 3.9
class Stack: #класс стека
    def __init__(self): #основной метод - создание массива(стека)
        self.__a = []
    def push(self): #если изменение, то добавляет элемент
        if 1 in self.__a:
            self.__a.pop(self.__a.index(1))
        self.__a.append(-1)
    def delete(self): #если признание, то удаляет элемент
        if -1 in self.__a:
            self.__a.pop(self.__a.index(-1))
        self.__a.append(1)
    def lenst(self): #проверка, есть ли в стеке элементы
        return len(self.__a)

a = []
with open("history_mirror.txt", "r", encoding="utf-8") as file: #открывается файл для занесения в двумерный массив
    q = file.readline()
    for row in file.readlines():
        a.append(row.replace("\n", "").replace("-", "").split("="))

st = Stack() #создание стека
for row in a: #проверка изменения и призания
    if row[2] == "Изменение характера":
        st.push()
    elif row[2] == "Признание своей уникальности":
        st.delete()
if st.lenst() != 0: #проверка длины стека
    print("Запросы не изолированные")
else:
    print("Запросы изолированные")