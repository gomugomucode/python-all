from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def pay_slip(self):
        # type(self).__name__ automatically gets "FullTimeEmployee", "Contractor", etc.
        return f"{self.name} | Pay : Rs. {self.calculate_pay()} | {type(self).__name__}"


class FullTimeEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def __str__(self):
        return f"Full Time Employee: {self.name} | Salary: Rs. {self.salary}"


class PartTimeEmployee(Employee):

    def __init__(self, name, rate, hours):  
        super().__init__(name)
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f"Part Time Employee: {self.name} | Hours: {self.hours} | Rate: Rs. {self.rate}"


class Contractor(Employee):

    def __init__(self, name, project_fee, number_of_projects):
        super().__init__(name)
        self.project_fee = project_fee
        self.number_of_projects = number_of_projects

    def calculate_pay(self):
        return self.number_of_projects * self.project_fee

    def __str__(self):
        return f"Contractor: {self.name} | Projects: {self.number_of_projects} | Fee: Rs. {self.project_fee}"


if __name__ == "__main__":
    staff = [
        FullTimeEmployee("Asha", 60000),
        PartTimeEmployee("Bibek", 500, 80),  
        Contractor("Chen", 15000, 3),  
    ]

    for emp in staff:
        print(emp.pay_slip())

    total = sum(e.calculate_pay() for e in staff)
    print("Total payroll:", total)  # Output: 145000
