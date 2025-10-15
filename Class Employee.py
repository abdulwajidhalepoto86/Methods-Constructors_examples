class Employee:
    total_employees = 0   
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1 

    def display_details(self):   
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls): 
        print(f"Total Employees: {cls.total_employees}")

emp1 = Employee("Abdul Wajid", 70000)
emp2 = Employee("Ismail ", 60000)

emp1.display_details()
emp2.display_details()
Employee.show_total_employees()