class Train():
    def __init__(self, train_number = "P123", destination = "City A", departure_time = "10:00", platform = 1,):
        self.train_number = train_number
        self.destination = destination
        self.departure_time = departure_time
        self.platform = platform
    
    def __str__(self):
        return f"Номер поезда: {self.train_number} - Пункт назначения: {self.destination} - Время отправления: {self.departure_time} - Номер платформы: {self.platform}"
    
class PassengerTrain(Train):
    def __init__(self, train_number = "P123", destination = "City A", departure_time = "10:00", platform = 1, passenger_capacity=200):
        super().__init__(train_number, destination, departure_time, platform)
        self.passenger_capacity = passenger_capacity

class FreightTrain(Train):
    def __init__(self, train_number = "P123", destination = "City A", departure_time = "10:00", platform = 1, cargo_capacity=5000):
        super().__init__(train_number, destination, departure_time, platform)
        self.cargo_capacity = cargo_capacity

class TrainStation():
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def remove_train(self, train):
        self.trains.remove(train)

    def list_trains(self):
        print("Поезда на станции:")
        for train in self.trains:
            print(train)

# Trains = Train()
# Trains.get_info()
# Pasha = TrainStation()
# Pasha.list_trains

passenger_train = PassengerTrain("P123", "City A", "10:00", 1, passenger_capacity=200)
freight_train = FreightTrain("F456", "City B", "12:00", 2, cargo_capacity=5000)
print(freight_train, passenger_train)
train_station = TrainStation()
train_station.add_train(passenger_train)
train_station.add_train(freight_train)
train_station.list_trains()
train_station.remove_train(passenger_train)
train_station.list_trains()