from datetime import datetime
import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.set_name(name)
        self.set_phone(phone)
        self.set_birthday(birthday)
        self.set_email(email)
        self.set_specialty(specialty)

    def calculate_age(self):
        if hasattr(self, '_birthday'):
            today = datetime.now()
            birthday_date = datetime.strptime(self._birthday, "%d.%m.%Y")
            age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
            return age
        else:
            print("Дата рождения не установлена.")
            return None

    def calculate_salary(self):
        pass  # This method will be overridden by subclasses

    def set_name(self, value):
        if re.match(r'^[A-Za-zА-яёЁ]+$', value):
            self._name = value
        else:
            print("Имя должно содержать только буквы.")

    def get_name(self):
        return self._name

    def set_phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self._phone = value
        else:
            print("Номер телефона должен соответствовать формату +373 и содержать 8 цифр.")

    def set_birthday(self, value):
        if re.match(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(1960|19[7-9]\d|200[0-7])$', value):
            self._birthday = value
        else:
            print("Дата рождения должна быть в формате ДД.ММ.ГГГГ, год должен быть между 1960 и 2007.")

    def set_email(self, value):
        if re.match(r'^[\w.-]+@\w+\.\w{2,4}$', value):
            self._email = value
        else:
            print("Некорректный формат электронной почты.")

    def set_specialty(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self._specialty = value
        else:
            print("Специальность должна состоять только из букв и быть длиной от 4 до 20 символов.")

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, specialty)
        self.set_hourly_rate(hourly_rate)
        self.set_hours_worked(hours_worked)

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

    def set_hourly_rate(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self._hourly_rate = float(value)
        else:
            print("Некорректная почасовая ставка. Введите правильное числовое значение.")

    def set_hours_worked(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self._hours_worked = float(value)
        else:
            print("Некорректное количество отработанных часов. Введите правильное числовое значение.")

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthly_salary):
        super().__init__(name, phone, birthday, email, specialty)
        self.set_monthly_salary(monthly_salary)

    def calculate_salary(self):
        return self._monthly_salary

    def set_monthly_salary(self, value):
        if re.match(r'^\d+(\.\d+)?$', str(value)):
            self._monthly_salary = float(value)
        else:
            print("Некорректная месячная зарплата. Введите правильное числовое значение.")
