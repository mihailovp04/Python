import re

def validate_employee_data(last_name, first_name, department, salary):
    if not re.match(r'^[a-zA-Zа-яА-Я-]+$', last_name):
        return False
    if not re.match(r'^[a-zA-Zа-яА-Я-]+$', first_name):
        return False
    if not re.match(r'^[a-zA-Zа-яА-Я]+(?: [a-zA-Zа-яА-Я]+)?$', department):
        return False
    if not (1000.00 <= salary <= 77000.00):
        return False
    return True

def write_employee_data(filename):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    department = input("Введите департамент: ")
    salary_input = input("Введите зарплату: ")
    
    try:
        salary = float(salary_input)
    except ValueError:
        print("Некорректный ввод зарплаты. Зарплата должна быть числом.")
        return

    if validate_employee_data(last_name, first_name, department, salary):
        with open(filename, 'a') as file:
            file.write(f"{last_name} {first_name} {department} {salary}\n")
        print("Данные успешно добавлены.")
    else:
        print("Некорректные данные.")

def read_employee_data(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 4:
                    employees.append(parts)
    except FileNotFoundError:
        print("Файл не найден.")
    return employees

def calculate_average_salary(employees):
    if not employees:
        return 0
    total_salary = sum(float(emp[3]) for emp in employees)
    return total_salary / len(employees)

def find_employee_with_max_salary(employees):
    if not employees:
        return []
    max_salary = max(float(emp[3]) for emp in employees)
    return [emp for emp in employees if float(emp[3]) == max_salary]

def find_employee_with_min_salary(employees):
    if not employees:
        return []
    min_salary = min(float(emp[3]) for emp in employees)
    return [emp for emp in employees if float(emp[3]) == min_salary]

def calculate_average_salary_by_department(employees):
    departments = {}
    for last_name, first_name, department, salary in employees:
        if department not in departments:
            departments[department] = []
        departments[department].append(float(salary))
    averages = {dep: sum(sals) / len(sals) for dep, sals in departments.items()}
    return averages
