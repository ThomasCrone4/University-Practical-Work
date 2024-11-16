from Car_manager import CarManager

def main():
    # Create the car manager
    my_car_manager = CarManager()

    print("Should create manager object/instance/value")
    print(my_car_manager)

    print("Get list of cars and print it")
    print(my_car_manager.get_cars())

    print("Find all cars that are older than 11 years old")
    print(my_car_manager.get_cars_older_than(11))

    print("Find all cars that are a hatchback")
    print(my_car_manager.get_cars_of_type("hatchback"))

    print("Add a new car to the file")
    my_car_manager.add_to_file("Lambo", "2003", "Fast", "Red", "Sports")
    print(my_car_manager.get_cars())

    my_car_manager.remove_from_file("Lambo")
    print(my_car_manager.get_cars())

# Run the main method
main()