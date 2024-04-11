import re

def check_phone_number(phone_number):
    phone_pattern = r'^(00373\d{8}|\+373\d{8}|\d{8})$'
    if re.match(phone_pattern, phone_number):
        return True
    else:
        return False

input_phone_number = input("Введите номер телефона: ")

try:
    if check_phone_number(input_phone_number):
        print("Номер телефона корректный.")
    else:
        print("Некорректный формат номера телефона.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
