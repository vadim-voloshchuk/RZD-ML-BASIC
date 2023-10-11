# Исходные данные
trains = []

def add_train(num, direction,time_start, time_arrive):
    train = {
        "num": num,
        "direction": direction,
        "time_start": time_start, 
        "time_arrive": time_arrive
    }

    trains.append(train)

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


add_train(10, "восток", 123412, 14241)
add_train(5, "восток", 123412, 14241)
info_trains()
del_train(10)
info_trains()