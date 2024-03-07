def add_writer(writers, name):
    if name in writers:
        print("Этот автор уже добавлен.")
    else:
        writers[name] = []
        print(f"Автор {name} добавлен.")
    return writers

def add_book_to_writer(writers, name, title):
    if name not in writers:
        print("Ошибка! Такого автора нет в списке!")
    elif title in writers[name]:
        print(f"Ошибка! Книга '{title}' уже есть у автора: {name}.")
    else:
        writers[name].append(title)
        print(f"Книга '{title}' добавлена автору: {name}.")
    return writers


def view_writers(writers):
    if not writers:
        print("Список авторов пуст.")
    else:
        print("Список авторов и их книг:")
        for writer, books in writers.items():
            print(f"{writer}: {', '.join(books)}")

def count_books_of_writers(writers):
    if not writers:
        print("Список авторов пуст.")
    else:
        print("Количество книг у каждого автора:")
        for writer, books in writers.items():
            print(f"{writer}: {len(books)}")

def remove_writer(writers, name):
    if name not in writers:
        print("Такого автора нет в списке.")
    else:
        del writers[name]
        print(f"Автор {name} и все его книги успешно удалены.")
    return writers
