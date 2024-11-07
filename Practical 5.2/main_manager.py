from Car_manager import CarManager

def main():
    # Create the car manager
    my_car_manager = CarManager()

    print("Should create manager object/instance/value")
    print(my_car_manager)

    # Requires __repr__ method be defined in car.py else you get
    # something like this [<car.Car object at 0x7f8787e74f70>,
    # <car.Car object at 0x7f8787e42d30>, <car.Car object at
    # 0x7f8787e42d60>, <car.Car object at 0x7f8787e42c10>]
    print("Get list of cars and print it")
    print(my_car_manager.get_cars())

    print("Find all cars that are older than 11 years old")
    print(my_car_manager.get_cars_older_than(11))

    print("Find all cars that are a hatchback")
    print(my_car_manager.get_cars_of_type("hatchback"))


# Run the main method
main()