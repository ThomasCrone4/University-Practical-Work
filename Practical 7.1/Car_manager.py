from Class_car import car

class CarManager():

    def __init__(self):
        self.__cars = []
        with open(r"C:\Users\thoma\OneDrive - Newcastle University\Practicals\University-Practicals\Practical 7.1\cars.csv", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:  # Ensure correct number of parts
                    self.__cars.append(car(parts[0], parts[1], parts[2], parts[3], parts[4])) 

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
    
    def add_to_file(self, make, year, model, category, color):
        with open(r"C:\Users\thoma\OneDrive - Newcastle University\Practicals\University-Practicals\Practical 7.1\cars.csv", "a") as f:
            f.write(f"{make}, {year}, {model}, {color}, {category}\n")

    def remove_from_file(self, remove_car):
        with open(r"C:\Users\thoma\OneDrive - Newcastle University\Practicals\University-Practicals\Practical 7.1\cars.csv", "r") as f:
            read_data = f.readlines()

        with open(r"C:\Users\thoma\OneDrive - Newcastle University\Practicals\University-Practicals\Practical 7.1\cars.csv", "w") as f:
            for line in read_data:
                if remove_car not in line:
                    f.write(line)
            
            