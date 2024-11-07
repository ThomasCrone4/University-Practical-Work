#Practical 5.2 1034
from typing import Any
import datetime


class car():
    def __init__(self, year, make, color, category):
        if (year is None) or (make is None) or (color is None) or (category is None):
            raise ValueError("A variable passed to car class if none, ensure all variables hold values")
        self.__year = year
        self.__make = make
        self.__top_speed = 25
        self.__color = color
        self.__category = category
        self.__speed = 0
    
    def accelerate(self):
        if self.__speed < self.__top_speed:
            self.__speed = self.__speed + 5
        else:
            self.__speed = self.__top_speed
            print("Top speed has been reached")
        

    def brake(self):
        if self.__speed > 0:
            self.__speed -= 5
        else: 
            self.__speed = 0
            print("Car has stopped")    


    def get_speed(self):
        return self.__speed
    
    def get_year(self):
        return self.__year
    
    def get_make(self):
        return self.__make
    
    def get_top_speed(self):
        return self.__top_speed
    
    def get_color(self):
        return self.__color
    
    def get_category(self):
        return self.__category
    
    def get_age(self):
        return self.__age
    
    def set_year(self, new_year):
        self.__year = new_year
        
    def set_make(self, new_make):
        self.__make = new_make

    def set_top_speed(self, new_top_speed):
        self.__top_speed = new_top_speed

    def set_color(self, new_color):
        self.__color = new_color

    def set_category(self, new_category):
        self.__category = new_category

    def __get_age(self):
        year_of_model = int(self.get_year())
        current_year = int(datetime.date.today().year)
        age_in_years = current_year - year_of_model
        return age_in_years
    
    def is_older_than(self, age):
        return self.__get_age() > age
    
    def __str__(self):
        out = "Car: {year}, {age} years old, {make}, {color}, {category}"
        return out.format(year = self.get_year(),
                          age = self.__get_age(),
                          make = self.get_make(),
                          color = self.get_color(),
                          category = self.get_category())
    
    def __repr__(self):
        out = "Car('{year_of_model}','{make}','{colour}','{category}')"
        return out.format(year_of_model = self.get_year(),
                          make = self.get_make(),
                          colour = self.get_color(),
                          category = self.get_category())

