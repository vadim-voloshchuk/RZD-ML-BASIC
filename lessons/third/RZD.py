import os

trains = []

def add_train(num, direction,time_start, time_arrive):
    train = {
        "num": num,
        "direction": direction,
        "time_start": time_start, 
        "time_arrive": time_arrive
    }

    trains.append(train)

# add_train(10, "восток", 123412, 14241)

def info_trains():
    print("Список поездов:")
    for train in trains:
        print("Номер поезда: " + str(train['num']))
        print("Направление: " + str(train['direction']))
        print("Время отбытия: " + str(train['time_start']))
        print("Время прибытия: " + str(train['time_arrive']))
        print('___________________________________________________\n')

def find_train(in_direction):
    for train in trains:
        if train['direction'] == in_direction:
            print("Номер поезда: " + str(train['num']))
            print("Направление: " + str(train['direction']))
            print("Время отбытия: " + str(train['time_start']))
            print("Время прибытия: " + str(train['time_arrive']))
            print('___________________________________________________\n')
        
def del_train(num):
    for train in trains:
        if train['num'] == num:
            trains.pop(trains.index(train))

def update_train(num, key, value):
    for train in trains:
        if train['num'] == num:
            train[key] = value


add_train(10, "восток", 123412, 14241)
# add_train(5, "восток", 123412, 14241)
# info_trains()
# update_train(10, 'direction', 'север')
# info_trains()

while True:
    os.system('cls')
    print("Главное меню")
    print('1 - Добавить поезд')
    print('2 - Получить информацию о поезде')
    print('3 - Найти поезда по направлению')
    print('4 - Удалить поезд')
    print('5 - Обновить информацию о поезде')
    print('6 - Выход')
    
    choice = input('Выберите действие: ')

    if choice == "1":
        print("Чтобы добавить поезд введите:")
        num = int(input('Введите номер поезда'))
        direction = input('Введите направление поезда')
        time_start = input('Введите time_start поезда')
        time_arrive = input('Введите time_arrive поезда')

        add_train(num, direction,time_start, time_arrive)
        print("Поезд успешно добавлен")
        input("Нажмите Enter, чтобы продолжить...")
    
    if choice == "2":
        info_trains()
        input("Нажмите Enter, чтобы продолжить...")
    
    if choice == "3":
        direction = input('Введите направление поезда: ')
        del_train(num)
        input("Нажмите Enter, чтобы продолжить...")
    
    if choice == "4":
        direction = input('Введите номер поезда для удаления: ')
        find_train(direction)
        print("Поезд успешно удален")
        input("Нажмите Enter, чтобы продолжить...")
    
    if choice == "6":
        break

