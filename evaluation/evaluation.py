from functions import *
def main():
    writers = {}

    while True:
        print("\nЧего желаете?:")
        print("1. Добавить автора")
        print("2. Добавить книгу к существующему автору")
        print("3. Просмотреть список авторов и их книг")
        print("4. Вывод количества книг у авторов")
        print("5. Удаление автора и его книг")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя автора: ")
            writers = add_writer(writers, name)
        elif choice == "2":
            name = input("Введите имя существующего автора: ")
            if name not in writers:
                print("Ошибка! Такого автора нет в списке!")
                continue
            title = input("Введите название книги: ")
            writers = add_book_to_writer(writers, name, title)
        elif choice == "3":
            view_writers(writers)
        elif choice == "4":
            count_books_of_writers(writers)
        elif choice == "5":
            name = input("Введите имя автора, которого хотите удалить: ")
            writers = remove_writer(writers, name)
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Ошибка!!! Неверный ввод.")
main()
