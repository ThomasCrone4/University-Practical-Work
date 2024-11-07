from Class_car import car

class CarManager():

    def __init__(self):
        self.__cars = []
        with open("C:/Users/thoma/OneDrive - Newcastle University/Practicals/Programming 1034/Practical 5.2/cars.csv", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                self.__cars.append(car(parts[1],parts[0],parts[4],parts[3]))

    def get_cars(self):
        return self.__cars
    
    def get_cars_older_than(self, age):
        older_cars = []
        for car in self.__cars:
            if car.is_older_than(age):
                older_cars.append(car)
        return older_cars

    def get_cars_of_type(self, category):
        valid_cars = []
        for car in self.__cars:
            if car.get_category() == category:
                valid_cars.append(car)
        return valid_cars