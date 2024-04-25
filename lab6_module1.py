from datetime import datetime
import re

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__specialty = specialty

    def calculateAge(self):
        """Рассчитать возраст сотрудника."""
        today = datetime.now()
        birthday_date = datetime.strptime(self.__birthday, "%d.%m.%Y")
        age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
        return age

    def _calculateSalary(self):
        """Вычислить зарплату (метод для переопределения)."""
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if re.match(r'^[a-zA-Z]+$', value):
            self.__name = value
        else:
            raise ValueError("Неверное имя. Допустимы только буквы.")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self.__phone = value
        else:
            raise ValueError("Номер телефона должен соответствовать формату +373 и следовать за ним 8 цифр.")

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if re.match(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.(1960|19[7-9]\d|200[0-7])$', value):
            self.__birthday = value
        else:
            raise ValueError("Дата рождения должна быть в формате ДД.ММ.ГГГГ и год должен быть между 1960 и 2007.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if re.match(r'^[\w.-]{2,20}@\w{4,7}\.\w{2,4}$', value):
            self.__email = value
        else:
            raise ValueError("Неверный формат электронной почты.")

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self.__specialty = value
        else:
            raise ValueError("Специальность должна быть от 4 до 20 букв.")

class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hourly_rate, hours_worked):
        super().__init__(name, phone, birthday, email, specialty)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def _calculateSalary(self):
        return self.__hourly_rate * self.__hours_worked

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self.__hourly_rate = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        self.__hours_worked = value

class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthly_salary):
        super().__init__(name, phone, birthday, email, specialty)
        self.__monthly_salary = monthly_salary

    def _calculateSalary(self):
        return self.__monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        self.__monthly_salary = value
