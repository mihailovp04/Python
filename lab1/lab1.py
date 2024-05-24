#task3
name=input("Your name?")
print("Hello",name, "how are you?")
#task4
number=21
pi=3.14
ministring="Hello world"
bigstring="""Hello world!
My name is Piotr!
I am 19"""
#task5
print(type(ministring))
print(type(pi))
#task6
print(len(ministring))
#task7
print(ministring.upper())
#task8
print(len(ministring))
print(ministring[9:12])
#zadanie2


txt = "More results from text..."
substr = txt[4:12] 
print(substr)
print(substr.strip())  # Этим методом мы удаляем пробелы в начале или в конце строки

txt = "More results from text..."
print(txt.split())  # Этим методом мы разбиваем строку на подстроки, если находит экземпляры разделителя в строке. Подстроки сохраняются как элементы списка

# Форматируем строку, подставляя значение переменной в нужное место
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))  # Этим методом выводим отформатированную строку, где значение переменной age подставлено вместо фигурных скобок




