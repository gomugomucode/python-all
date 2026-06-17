from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def pay_slip(self):
        return f"{self.name} | Pay : Rs. {self.calculate_pay()}"


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def __str__(self):
        return f"Full Time Employee: {self.name} | Salary: Rs. {self.salary}"

    def pay_slip(self):
        return super().pay_slip() + f" | Full Time Employee"


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate

    def __str__(self):
        return f"Part Time Employee: {self.name} | Hours: {self.hours} | Rate: Rs. {self.rate}"

    def pay_slip(self):
        return super().pay_slip() + f" | Part Time Employee"


class Contractor(Employee):
    def __init__(self, name, number_of_projects, project_fee):
        super().__init__(name)
        self.number_of_projects = number_of_projects
        self.project_fee = project_fee

    def calculate_pay(self):
        return self.number_of_projects * self.project_fee

    def __str__(self):
        return f"Contractor: {self.name} | Projects: {self.number_of_projects} | Fee: Rs. {self.project_fee}"
    
    def pay_slip(self):
        return super().pay_slip() + f" | Contractor"


if __name__ == "__main__":
    staff = [
        FullTimeEmployee("Asha", 60000),
        PartTimeEmployee("Bibek", 500, 80),
        Contractor("Chen", 15000, 3),
    ]

    for emp in staff:
        print(emp.pay_slip())
    # Asha | Pay: Rs 60000
    # Bibek | Pay: Rs 40000 (500 x 80)
    # Chen | Pay: Rs 45000 (15000 x 3)
    total = sum(e.calculate_pay() for e in staff)
    print("Total payroll:", total)  # 145000
# Employee("Test") # TypeError: Can't instantiate abstract class Employee
