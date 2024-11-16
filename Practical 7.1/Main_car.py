#Practical 5.2 main()
from Class_car import car
import datetime

def main():
    my_car1 = car("Toyota", "2004","Commuter", "Red", "SUV")
    while my_car1.get_speed() < 20:
        my_car1.accelerate()
        print (f" car1's speed is: {my_car1.get_speed()}")

    my_car1.accelerate()

    while my_car1.get_speed() > 0:
        my_car1.brake()
        print (f" car1's speed is: {my_car1.get_speed()}")

    my_car1.brake()

    my_car1.set_top_speed(100)
    print("New stop speed: {} ".format(my_car1.get_top_speed()))
    print(my_car1)

main()
    
