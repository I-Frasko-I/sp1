users_db = {
    "admin": {"password": "admin123", "role": "admin", "history": ['Акции']},
    "user1": {"password": "user123", "role": "user", "history": ['Ипотека']},
}

products = []

cart = []

def authenticate():
    print("\n--- Авторизация ---")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if username in users_db and users_db[username]["password"] == password:
        print(f"\nДобро пожаловать, {username}!")
        return username, users_db[username]["role"]
    else:
        print("Ошибка: Неверный логин или пароль.")
        return None, None

def add_product():
    print("\n--- Добавление товара ---")
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    products.append({"name": name, "price": price, "quantity": quantity})
    print(f"Товар '{name}' успешно добавлен!")

def remove_product():
    print("\n--- Удаление товара ---")
    view_products()
    name = input("Введите название товара для удаления: ")
    for product in products:
        if product["name"] == name:
            products.remove(product)
            print(f"Товар '{name}' успешно удален!")
            return
    print("Ошибка: Товар не найден.")

def view_products():
    pass


def edit_product():
    print("\n--- Редактирование товара ---")
    view_products()
    name = input("Введите название товара для редактирования: ")
    for product in products:
        if product["name"] == name:
            print("Введите новые данные (оставьте пустым для пропуска):")
            new_name = input("Новое название: ")
            new_price = input("Новая цена: ")
            new_quantity = input("Новое количество: ")

            if new_name:
                product["name"] = new_name
            if new_price:
                product["price"] = float(new_price)
            if new_quantity:
                product["quantity"] = int(new_quantity)

            print("Товар успешно обновлен!")
            return
    print("Ошибка: Товар не найден.")

def add_user():
    print("\n--- Добавление пользователя ---")
    username = input("Введите логин нового пользователя: ")
    if username in users_db:
        print("Ошибка: Пользователь уже существует.")
        return
    password = input("Введите пароль: ")
    role = input("Введите роль (user/admin): ").lower()
    if role not in ["user", "admin"]:
        print("Ошибка: Неверная роль.")
        return
    users_db[username] = {"password": password, "role": role, "history": []}
    print(f"Пользователь '{username}' успешно добавлен.")

def remove_user():
    print("\n--- Удаление пользователя ---")
    username = input("Введите логин пользователя для удаления: ")
    if username in users_db and username != "admin":
        del users_db[username]
        print(f"Пользователь '{username}' успешно удален.")
    else:
        print("Ошибка: Пользователь не найден или это администратор.")

def edit_user():
    print("\n--- Редактирование пользователя ---")
    username = input("Введите логин пользователя: ")
    if username in users_db and username != "admin":
        print("Введите новые данные (оставьте пустым для пропуска):")
        new_password = input("Новый пароль: ")
        new_role = input("Новая роль (user/admin): ").lower()
        if new_password:
            users_db[username]["password"] = new_password
        if new_role in ["user", "admin"]:
            users_db[username]["role"] = new_role
        print("Данные пользователя обновлены.")
    else:
        print("Ошибка: Пользователь не найден или это администратор.")

def view_statistics():
    print("\n--- Статистика ---")
    print(f"Общее количество пользователей: {len(users_db)}")
    print(f"Общее количество товаров: {len(products)}")

    popular_products = sorted(products, key=lambda x: x["quantity"], reverse=True)
    print("\nПопулярные товары (по количеству оставшихся):")
    for product in popular_products[:5]:
        print(f"{product['name']}: осталось {product['quantity']}")

def view_user_history():
    print("\n--- История покупок пользователей ---")
    for user, data in users_db.items():
        print(f"\nПользователь: {user}")
        if not data["history"]:
            print("История покупок пуста.")
        else:
            for item in data["history"]:
                print(f"{item['name']} - {item['quantity']} шт. по цене {item['price']}")

def view_products():
    print("\n--- Список товаров ---")
    if not products:
        print("Список товаров пуст.")
        return
    print(f"{'Название':<15}{'Цена':<10}{'Количество':<10}")
    for product in products:
        print(f"{product['name']:<15}{product['price']:<10}{product['quantity']:<10}")

def sort_products():
    print("\n--- Сортировка товаров ---")
    print("1. По названию\n2. По цене\n3. По количеству")
    choice = input("Выберите критерий сортировки (1/2/3): ")
    if choice == "1":
        products.sort(key=lambda x: x['name'])
    elif choice == "2":
        products.sort(key=lambda x: x['price'])
    elif choice == "3":
        products.sort(key=lambda x: x['quantity'])
    else:
        print("Ошибка: Неверный выбор.")
        return
    print("Товары отсортированы!")
    view_products()

def filter_products():
    print("\n--- Фильтрация товаров ---")
    min_price = float(input("Введите минимальную цену: "))
    max_price = float(input("Введите максимальную цену: "))
    print(f"\nТовары в диапазоне цен от {min_price} до {max_price}:")
    filtered = [p for p in products if min_price <= p['price'] <= max_price]
    if not filtered:
        print("Нет товаров в заданном диапазоне.")
        return
    print(f"{'Название':<15}{'Цена':<10}{'Количество':<10}")
    for product in filtered:
        print(f"{product['name']:<15}{product['price']:<10}{product['quantity']:<10}")

def add_to_cart():
    print("\n--- Добавление товара в корзину ---")
    view_products()
    name = input("Введите название товара для добавления в корзину: ")
    for product in products:
        if product["name"] == name:
            quantity = int(input("Введите количество: "))
            if quantity <= product["quantity"]:
                cart.append({"name": product["name"], "price": product["price"], "quantity": quantity})
                product["quantity"] -= quantity
                print(f"{quantity} шт. товара '{name}' добавлено в корзину.")
                return
            else:
                print("Ошибка: Недостаточное количество товара на складе.")
                return
    print("Ошибка: Товар не найден.")

def view_cart():
    print("\n--- Ваша корзина ---")
    if not cart:
        print("Корзина пуста.")
        return
    total = 0
    print(f"{'Название':<15}{'Цена':<10}{'Количество':<10}{'Сумма':<10}")
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']:<15}{item['price']:<10}{item['quantity']:<10}{subtotal:<10}")
    print(f"\nОбщая сумма: {total:.2f}")

def checkout(username):
    if not cart:
        print("Корзина пуста. Покупка невозможна.")
        return
    print("\n--- Завершение покупки ---")
    view_cart()
    confirm = input("Подтвердите покупку? (y/n): ").lower()
    if confirm == "y":
        users_db[username]["history"].extend(cart)
        cart.clear()
        print("Покупка успешно завершена!")
    else:
        print("Покупка отменена.")

def view_purchase_history(username):
    print("\n--- История покупок ---")
    history = users_db[username]["history"]
    if not history:
        print("История покупок пуста.")
        return
    print(f"{'Название':<15}{'Цена':<10}{'Количество':<10}")
    for item in history:
        print(f"{item['name']:<15}{item['price']:<10}{item['quantity']:<10}")

def update_account(username):
    print("\n--- Обновление учетной записи ---")
    new_password = input("Введите новый пароль: ")
    users_db[username]["password"] = new_password
    print("Пароль успешно обновлен!")

def admin_menu():
    while True:
        print("\n--- Меню администратора ---")
        print("1. Добавить товар\n2. Удалить товар\n3. Редактировать товар")
        print("4. Управление пользователями\n5. Просмотреть статистику\n6. История действий пользователей\n7. Выйти")
        choice = input("Выберите действие (1-7): ")
        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            user_management_menu()
        elif choice == "5":
            view_statistics()
        elif choice == "6":
            view_user_history()
        elif choice == "7":
            print("Выход из системы.")
            break
        else:
            print("Ошибка: Неверный ввод.")

def user_management_menu():
    while True:
        print("\n--- Управление пользователями ---")
        print("1. Добавить пользователя\n2. Удалить пользователя\n3. Редактировать пользователя\n4. Назад")
        choice = input("Выберите действие (1-4): ")
        if choice == "1":
            add_user()
        elif choice == "2":
            remove_user()
        elif choice == "3":
            edit_user()
        elif choice == "4":
            break
        else:
            print("Ошибка: Неверный ввод.")


def user_menu(username):
    while True:
        print("\n--- Меню пользователя ---")
        print("1. Просмотреть товары\n2. Добавить товар в корзину\n3. Просмотреть корзину")
        print("4. Завершить покупку\n5. История покупок\n6. Обновить учетную запись\n7. Выйти")
        choice = input("Выберите действие (1-7): ")
        if choice == "1":
            view_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout(username)
        elif choice == "5":
            view_purchase_history(username)
        elif choice == "6":
            update_account(username)
        elif choice == "7":
            print("Выход из системы.")
            break
        else:
            print("Ошибка: Неверный ввод.")

def main():
    while True:
        username, role = authenticate()
        if username:
            if role == "admin":
                admin_menu()
            elif role == "user":
                user_menu(username)

if __name__ == "__main__":
    main()
