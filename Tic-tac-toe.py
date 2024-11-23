"""Всеми известная игра крестики нолики.
    Все функции подписаны поэтому здесь писать что как работает нет смысла.
     Но добавлю план даного недо 'проекта':
     1. Сначало я сделал поле для игры и благодаря ему я смог придумать логику
     2. Сама логика игры, в этой функции есть две вложаные функции, первая это крестики, а вторая это нолики.
     3. Дабы функция отвечаюшая за логику игры осталась читаема и мой код небыл так сильно похож на говно-код,
        я сделал отдельную функцию где и определяется кто выиграл и ничью
     4. Главное меню. Я первая команда запускает саму команду, и при случае повторного запуска обнавляет и выход из системы."""

field = [1,2,3,4,5,6,7,8,9]

def playing_field():
    """Игровое поле
        каждое поле имеет свою нумерацию, для более лёгкой взаимодействия"""
    print("______" * 3)
    for i in range(3):
        print(" ",field[i*3], "|"," ",field[1+i*3], "|", " ",field[2+i*3], "|")
        print("______" * 3)

def play():
    """Сам процесс игры:
    1.функция cross отвечает за крестиуи
    2.функция zero отвечает за нолики
    В каждой функции заранее обределена условие, что если поле занято,
     то надо заново выбрать, дабы не выходила ошибка"""

    step = 0 #Сколько пользователь сделал шагов дабы победить
    playing_field()

    def cross(step):
        availability = int(input("Куда поставим крестик:"))
        if availability in field:
            ind = field.index(availability)
            field[ind] = "X"
            step += 1
            playing_field()
            if stop_play(step): #проверка на победу
                return "Подравляем"
            else:
                return zero(step)
        else:
            print("Даное поле уже нет(")
            return cross(step)

    def zero(step):
        availability = int(input("Куда поставим нолик:"))
        if availability in field:
            ind = field.index(availability)
            field[ind] = "O"
            step +=1
            playing_field()
            if stop_play(step): #проверка на победу
                return "Подравляем"
            else:
                return cross(step)
        else:
            print("Даное поле уже нет(")
            return zero(step)
    return cross(step)

def stop_play(step):
    """Функция определяет конец игры"""

    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
        (0, 4, 8), (2, 4, 6)  # диагональные линии
    )
    if step == 9:
        win = print("Ничья") #Не бейте меня пожалуста, знаю что уродливо
        return win, menu()
    for pos in win_combination:
        if (field[pos[0]] == field[pos[1]] and field[pos[1]] == field[pos[2]] and field[pos[1]] in ('X', 'O')):
            #Мы проверяем на сочитание комбинации для победы
            print(f'''Победил: {field[pos[0]]}''')
            print("Было сделано шагов", step)
            win = True
            menu()
    return win
def menu():
    """Меню, пока что сделал 2 вазможности, если добавлю, то  3  выводит стастистику"""
    while True:
        print("Выберите действие:")
        print("1. Играть")
        print("2. Выход")
        choice = int(input("Ведите цыфру команды:"))

        if choice == 1:
            global field #Обнавляем поле
            field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            play()
        elif choice == 2:
            break
menu()
