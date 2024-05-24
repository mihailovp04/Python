from lab6_module2 import Employee, HourlyEmployee, SalaryEmployee

def create_employee(cls, employee_type):
    print(f"\nСоздание сотрудника типа {employee_type}:")
    name = input("Введите имя: ")
    phone = input("Введите телефон (+373xxxxxxxx): ")
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    email = input("Введите email: ")
    specialty = input("Введите специальность: ")
    if cls is HourlyEmployee:
        hourly_rate = float(input("Введите почасовую ставку: "))
        hours_worked = float(input("Введите количество отработанных часов: "))
        return cls(name, phone, birthday, email, specialty, hourly_rate, hours_worked)
    elif cls is SalaryEmployee:
        monthly_salary = float(input("Введите месячную зарплату: "))
        return cls(name, phone, birthday, email, specialty, monthly_salary)
    else:
        return cls(name, phone, birthday, email, specialty)

def input_employees():
    general_employee = create_employee(Employee, "обычного")
    hourly_employee = create_employee(HourlyEmployee, "почасового")
    salary_employee = create_employee(SalaryEmployee, "с фиксированной оплатой")
    return general_employee, hourly_employee, salary_employee

def display_salaries(*employees):
    print("\nЗарплаты всех сотрудников:")
    for employee in employees:
        print(f"{employee.get_name()}: {employee.calculate_salary()}")

if __name__ == "__main__":
    general_employee, hourly_employee, salary_employee = input_employees()
    display_salaries(general_employee, hourly_employee, salary_employee)
