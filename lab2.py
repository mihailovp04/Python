#task b
my_list=[1,2,3,4,5,'lalala']    
print(my_list[0])
print(my_list[2])
my_list[1]=10
print(my_list[2:4])
print(type(my_list[2]))
print(len(my_list))
print(my_list[5].upper())
print(my_list[5].strip())
print(my_list[5].lower())
#task c
my_list2=[1,228,2, 1337 ]
print(type(my_list2[0]),type(my_list2[2]))
print(my_list2[0], my_list2[3])
print(my_list2[1:4])
print(max(my_list2))
print(min(my_list2))
print(sum(my_list2))
#task d
my_set={1,2,3,4,5,6,7,8,9,1,2,3}
print(my_set)
my_set.add(11)
my_set.remove(3)
print(my_set)
print(len(my_set))
print(max(my_set))
#task e
mySlovari={'team': 'Real Madrid',
           'year': 1902,
           'best player': 'Ronaldo',
           'Champions': 14}
mySlovari2={
    1: 'Miyagi',
    2:'Andy Panda',
    3: 'Stas Mihailov',
    4:'KDK'
}
print(mySlovari['team'])
print(mySlovari2[1])
print(mySlovari['team'].upper())
print(mySlovari2[2].split())
print(mySlovari2.keys())
print(len(mySlovari2[3]))
print(tuple(mySlovari['team']))
#task f
new_list=float(my_list[3])
print(new_list)
#task 2 (a)
items=[10,20,30]
text_items=['apple','banana','orange']
info_1 = "{} цена: ${}".format(text_items[0], items[0])
info_2 = "{} цена: ${}".format(text_items[1], items[1])
info_3 = "{} цена: ${}".format(text_items[2], items[2])
print(info_1,'\n',info_2,'\n',info_3,'\n')
#task 2(b)
age = input("Введите ваш возраст: ")
age = int(age)
future_age = age + 5
print("Через 5 лет вам будет " + str(future_age) + " лет.")
#task 2(c)
fruits=['Apple','Banana','Orange']
searchFruits=input('Enter fruit:')
print(searchFruits in fruits)
list_lalala={1,2,3,4,5,6,7,8,9}
searchNumber=int(input('Enter number:'))
print(searchNumber not in list_lalala)