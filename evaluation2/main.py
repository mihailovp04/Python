from functions import write_employee_data, read_employee_data, calculate_average_salary, \
    find_employee_with_max_salary, find_employee_with_min_salary, calculate_average_salary_by_department

def main():
    filename = "employees.txt"
    while True:
        print("1) Записать данные о зарплатах сотрудников")
        print("2) Вывести среднюю зарплату сотрудников")
        print("3) Вывести данные сотрудника с самой высокой зарплатой")
        print("4) Вывести данные сотрудника с наименьшей зарплатой")
        print("5) Вывести среднюю зарплату по каждому департаменту")
        print("6) Выход")
        choice = input("Выберите опцию: ")
        if choice == '1':
            write_employee_data(filename)
        elif choice == '2':
            employees = read_employee_data(filename)
            average = calculate_average_salary(employees)
            print("Средняя зарплата:", average)
        elif choice == '3':
            employees = read_employee_data(filename)
            max_salary_emp = find_employee_with_max_salary(employees)
            if max_salary_emp:
                print("Сотрудник с максимальной зарплатой:", max_salary_emp)
        elif choice == '4':
            employees = read_employee_data(filename)
            min_salary_emp = find_employee_with_min_salary(employees)
            if min_salary_emp:
                print("Сотрудник с минимальной зарплатой:", min_salary_emp)
        elif choice == '5':
            employees = read_employee_data(filename)
            averages = calculate_average_salary_by_department(employees)
            for department, average in averages.items():
                print(department + ":", "средняя зарплата", average)
        elif choice == '6':
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()
