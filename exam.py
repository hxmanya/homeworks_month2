import sqlite3

db_name = '''store.db'''


def get_stores(curs):
    """Получение списка всех магазинов."""
    curs.execute('SELECT store_id, title FROM store ORDER BY store_id')
    return curs.fetchall()


def get_products_by_store(curs, store_id) :
    """Получение всех продуктов для заданного магазина."""
    curs.execute('''
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    ''', (store_id,))
    return curs.fetchall()


def display_stores(curs):
    """Отображение списка магазинов."""
    stores = get_stores(curs)
    print("\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, "
          "для выхода из программы введите цифру 0:")
    for store_id, title in stores:
        print(f"{store_id}. {title}")


def display_products(curs, store_id):
    """Отображение продуктов выбранного магазина."""
    products = get_products_by_store(curs, store_id)

    if not products:
        print("\nВ данном магазине нет продуктов.")
        return

    print("\nПродукты в магазине:")
    for product in products:
        print(f"\nНазвание продукта: {product[0]}")
        print(f"Категория: {product[1]}")
        print(f"Цена: {product[2]}")
        print(f"Количество на складе: {product[3]}")





try:
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        while True:
            display_stores(cur)
            try:
                choice = int(input("\nВведите ID магазина (0 для выхода): "))
                if choice == 0:
                    print("Программа завершена.")
                    break
                display_products(cur, choice)
            except ValueError:
                print("Пожалуйста, введите корректный номер магазина.")

except sqlite3.Error as error:
    print(error)
