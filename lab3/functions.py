
def add_product(product_list, product):
    product_list.append(product)
    print("Товар успешно добавлен.")

def remove_product_by_index(product_list, index):
    if index < 1 or index > len(product_list):
        print("Ошибка")
        return
    del product_list[index - 1]
    print("Товар успешно удален.")

def remove_product_by_name(product_list, name):
    if name not in product_list:
        print("Ошибка: Такого товара нет в списке.")
        return
    product_list.remove(name)
    print("Товар успешно удален.")

def show_all_products(product_list):
    if not product_list:
        print("Список товаров пуст.")
        return
    print("Текущий ассортимент продуктов:")
    for i, product in enumerate(product_list, 1):
        print(f"{i}. {product}")
