# File name = emp.py
class Employee:
    def __init__(self, id_number, employee_name, department, title):
        self.__id_number = id_number;
        self.__employee_name = employee_name
        self.__department = department
        self.__title = title

    def get_id_number(self):
        return self.__id_number

    def get_employee_name(self):
        return self.__employee_name

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title
    
    def set_id_number(self, new_id):
        self.__id_number = new_id

    def set_employee_name(self, new_name):
        self.__employee_name = new_name

    def set_department(self, new_dept):
        self.__department = new_dept

    def set_title(self, new_title):
        self.__title = new_title

    def __str__(self):
        return 'Employee ID: {}, Name: {}, Department: {}, Title: {}'.format(self.__id_number, self.__employee_name, self.__department, self.__title)
    
class SalesAssistant(Employee):
    def __init__(self, id_number, employee_name, department, title, shift_number, pay_rate):
        super().__init__(self, id_number, employee_name, department, title)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate
    
    def set_shift_number(self, new_shift_number):
        self.__shift_number = new_shift_number

    def set_pay_rate(self, new_pay_rate):
        self.__pay_rate = new_pay_rate

class Supervisor(Employee):
    def __init__(self, id_number, employee_name, department, title, salary, bonus):
        Employee.__init__(self, id_number, employee_name, department, title)
        self.__salary = salary
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus
    
    def set_salary(self, new_salary):
        self.__salary = new_salary

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus