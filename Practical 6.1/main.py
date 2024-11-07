from emp import Employee, SalesAssistant, Supervisor

def main():
    Employee_1 = Employee(1, 'Bob', 'HR', 'Manager')
    Employee_2 = Employee(2, 'Matt', 'Owner', 'CEO')
    Employee_3 = Employee(3, 'Sean', 'Front desk', 'Reception')
    print(Employee_1)
    print(Employee_2)
    print(Employee_3)

    supervisor = Supervisor('12345', 'Jordan', 'Retail', 'Supervisor', 24000, 2000)
    print(supervisor)


main()