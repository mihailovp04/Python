#task1 
import datetime
import re

def calculate_age_in_days():
    today = datetime.date.today()
    
    date_input = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
    
    if not re.match(r"\d{4}-\d{2}-\d{2}", date_input):
        print("Дата введена некорректно. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")
        return
    
    year, month, day = map(int, date_input.split('-'))
    birth_date = datetime.date(year, month, day)
    
    delta = today - birth_date
    print(f"Вы прожили {delta.days} дней.")

calculate_age_in_days()
#task2
import calendar

def find_weekday_of_date():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    
    weekday = calendar.weekday(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"Эта дата ({year}-{month}-{day}) приходится на {days[weekday]}.")

find_weekday_of_date()
#task3
import math

def calculate_fall_time():
    try:
        height = float(input("Введите высоту падения в метрах: "))
        if math.isnan(height):
            print("Пожалуйста, введите числовое значение для высоты.")
            return
    except ValueError:
        print("Ошибка ввода. Необходимо ввести числовое значение.")
        return
    
    g = 9.8
    time = math.sqrt(2 * height / g)
    print(f"Время падения с высоты {height} метров составляет {time:.2f} секунд.")

calculate_fall_time()
