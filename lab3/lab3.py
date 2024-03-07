#task1
#a)
i = sum = 0
while i <= 4:
    sum += i
    i = i+1
print(sum)
#Этот код представляет собой цикл while, который начинается с i и sum, равными 0. 
#На каждой итерации i увеличивается на 1, а sum увеличивается на текущее значение i. 
#Цикл продолжается до тех пор, пока i не станет больше 4. Затем выводится значение sum. 
#b)
for char in 'PYTHON STRING':
  if char == ' ':
      break
  print(char, end='')
  if char == 'O':
      continue
  print('*', end='')
#Этот код также содержит цикл, но уже for, который проходит по каждому символу в строке 'PYTHON STRING'. 
  #На каждой итерации он проверяет, если текущий символ пробел, то прерывает цикл (при помощи break).
#Если символ не пробел, он выводит его. Если символ равен 'O', 
#то он переходит к следующей итерации без выполнения оставшейся части цикла (при помощи continue). 
#После каждого символа, кроме 'O', выводится '*'. Результат интерпретации этого кода будет: P*Y*T*H*ON*
  #task2 a)
value = input("Введите значение: ")
if value == '1':
    print("Вы ввели число один.")
elif value == '2':
    print("Вы ввели число два.")
else:
    print("Вы ввели что-то другое.")
    #task 2 b)
my_list = [1, 2, 3, 4, 2, 3, 2, 1, 2, 3]
value_to_count = 2
count = 0

for item in my_list:
    if item == value_to_count:
        count += 1

print(f"Значение {value_to_count} встречается {count} раз в списке.")

my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 2}
value_to_count = 3
count = 0

for key, value in my_dict.items():
    if value == value_to_count:
        count += 1

print(f"Значение {value_to_count} встречается {count} раз в словаре.")  
  
    #task 2 c)
umnojenie = lambda x, y: x * y
result = umnojenie(10, 10)
print("Результат умножения:", result)
#task 3 
from functions import add_product, remove_product_by_index, remove_product_by_name, show_all_products

product_list = ["Яблоко", "Банан", "Апельсин"]

while True:
    print("\nМеню:")
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в список")
    print("3. Удалить товар из списка")
    print("4. Выход")

    choice = input("Выберите опцию: ")

    if choice == "1":
        show_all_products(product_list)
    elif choice == "2":
        product = input("Введите название товара: ")
        add_product(product_list, product)
    elif choice == "3":
        if not product_list:
            print("Ошибка: Список товаров пуст.")
            continue
        print("1. Удалить по порядковому номеру")
        print("2. Удалить по названию")
        remove_choice = input("Выберите способ удаления: ")
        if remove_choice == "1":
            index = int(input("Введите порядковый номер товара: "))
            remove_product_by_index(product_list, index)
        elif remove_choice == "2":
            name = input("Введите название товара: ")
            remove_product_by_name(product_list, name)
        else:
            print("Ошибка: Неверный выбор.")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Ошибка: Неверный ввод.")

