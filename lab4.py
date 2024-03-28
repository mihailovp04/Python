age = int(input("Введите ваш возраст: "))
height = int(input("Введите ваш рост в см: "))
gender = input("Введите ваш пол (М или Ж): ")

your_weight = int(input("Введите ваш текущий вес в кг: "))
if gender == "М":
    ideal_weight = height - 100 - ((height - 150) / 4 + (age - 20)) / 4
elif gender == "Ж":
    ideal_weight = height - 100 - ((height - 150) / 2.5 + (age - 20)) / 6

print("Ваш идеальный вес в кг:", ideal_weight)

if your_weight < ideal_weight:
    print("Немножко поднажмите и наберите вес, чтобы быть в идеальной форме, а именно:", ideal_weight - your_weight, "кг")
    
    if 25 <= age <= 60:
        print("Идеальный возраст, чтобы начать занятия спортом и набрать килограммы мышц.")
else:
    print("Немножко потрудитесь и сбросьте вес, чтобы быть в идеальной форме, а именно:", your_weight - ideal_weight, "кг")
    
    if 25 <= age <= 60:
        print("Идеальный возраст, чтобы начать занятия спортом и сбросить лишний вес.")
    elif age > 60:
        print("С возрастом обмен веществ замедляется, и объем пищи необходимо снизить.")
