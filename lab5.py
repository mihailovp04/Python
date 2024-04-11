import re

def input_data():
    while True:
        try:
            last_name = input("Введите фамилию сотрудника: ").strip()
            first_name = input("Введите имя сотрудника: ").strip()
            department = input("Введите отдел, в котором работает сотрудник: ").strip()
            children = input("Введите количество детей меньше 18 лет: ").strip()

            if not re.match(r'^[A-Za-zА-Яа-я]{2,20}(-[A-Za-zА-Яа-я]{2,20})?$', last_name) or not re.match(r'^[A-Za-zА-Яа-я]{2,20}(-[A-Za-zА-Яа-я]{2,20})?$', first_name):
                print("Ошибка! Фамилия и имя должны содержать только буквы и быть длиной от 2 до 20 символов.")
                continue
            if not re.match(r'^[A-Za-zА-Яа-я0-9]+( [A-Za-zА-Яа-я0-9]+)?$', department):
                print("Название отдела должно состоять из букв и цифр.")
                continue
            if not re.match(r'^[0-9]|1[0-9]$', children):
                print("Количество детей должно быть от 0 до 19. Пожалуйста, попробуйте снова.")
                continue

            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"{last_name}\t{first_name}\t{department}\t{children}\n")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            print("Попытка записи завершена.")

def view_children_data():
    try:
        total_children = 0
        with open("data.txt", "r", encoding="utf-8") as file:
            for line in file:
                last_name, first_name, department, children = line.strip().split("\t")
                print(f"Фамилия: {last_name}, Имя: {first_name}, Отдел: {department}, Количество детей: {children}")
                total_children += int(children)
        print(f"Общее количество детей всех сотрудников: {total_children}")
    except FileNotFoundError:
        print("Файл данных не найден. Пожалуйста, сначала введите данные.")
    finally:
        print("Попытка чтения данных завершена.")

def view_childless_employees():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            for line in file:
                last_name, first_name, department, children = line.strip().split("\t")
                if children == "0":
                    print(f"Фамилия: {last_name}, Имя: {first_name} - бездетный сотрудник")
    except FileNotFoundError:
        print("Файл данных не найден. Пожалуйста, сначала введите данные.")
    finally:
        print("Попытка чтения списка бездетных сотрудников завершена.")

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Ввод данных сотрудника")
        print("2. Просмотр данных о детях сотрудников")
        print("3. Просмотр списка бездетных сотрудников")
        print("4. Выход из программы")
        
        choice = input("Выберите опцию: ").strip()
        
        if choice == "1":
            input_data()
        elif choice == "2":
            view_children_data()
        elif choice == "3":
            view_childless_employees()
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("Некорректный ввод, пожалуйста, выберите опцию от 1 до 4.")

main_menu()
