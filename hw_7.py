import sqlite3


db_name = '''hw.db'''

sql_to_create_products_table = '''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0,
    quantity INT NOT NULL DEFAULT 0
)'''


def create_table(sql):
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_product(product):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as error:
        print(error)

def add_products():
    sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES 
        ("жидкое мыло с запахом ванили", 175.50, 10),
        ("мыло детское", 45.90, 15),
        ("шампунь для волос", 120.00, 8),
        ("зубная паста", 85.30, 12),
        ("гель для душа", 95.60, 7),
        ("крем для рук", 65.40, 20),
        ("дезодорант", 110.80, 6),
        ("туалетная бумага", 35.20, 30),
        ("салфетки влажные", 55.90, 25),
        ("порошок стиральный", 180.50, 4),
        ("губка для посуды", 25.30, 40),
        ("освежитель воздуха", 95.70, 9),
        ("мочалка банная", 45.60, 15),
        ("зубная щетка", 70.40, 18),
        ("бумажные полотенца", 85.90, 22)
        '''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def update_product_quantity(product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as error:
        print(error)

def update_product_price(product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as error:
        print(error)

def delete_product(id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as error:
        print(error)

def print_all_products():
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            products = cursor.fetchall()
            print("\nВсе товары в базе данных:")
            print("-" * 70)
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1].capitalize()}, "
                      f"Цена: {product[2]}, Количество: {product[3]}")
            print("-" * 70)
    except sqlite3.Error as error:
        print(error)

def print_product(id):
    sql = '''SELECT * FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            products = cursor.fetchall()
            print(f"\nТовар с id: {id}")
            print("-" * 70)
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1].capitalize()}, "
                      f"Цена: {product[2]}, Количество: {product[3]}")
            print("-" * 70)
    except sqlite3.Error as error:
        print(error)


def print_filtered_products(price_limit = 100.0, quantity_limit = 5):
    sql = '''SELECT * FROM products WHERE price <=  ? AND quantity >= ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            products = cursor.fetchall()
            print(f"\nТовары дешевле {price_limit} сом и количеством больше {quantity_limit} шт:")
            print("-" * 70)
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1].capitalize()}, "
                      f"Цена: {product[2]}, Количество: {product[3]}")
            print("-" * 70)
    except sqlite3.Error as error:
        print(error)



def search_products_by_name(search_term):
    search_term = search_term.lower()
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (f"%{search_term}%",))
            products = cursor.fetchall()
            print(f"\nРезультаты поиска по запросу '{search_term}':")
            print("-" * 70)
            for product in products:
                print(f"ID: {product[0]}, Название: {product[1].capitalize()}, "
                      f"Цена: {product[2]}, Количество: {product[3]}")
            print("-" * 70)

    except sqlite3.Error as error:
        print(error)


if __name__ == '__main__':
    # create_table(sql_to_create_products_table)
    # add_products()
    print_all_products()
    insert_product(('ручной порошок', 140.5, 15))
    print_product(16)
    update_product_quantity((18, 16))
    update_product_price((150, 16))
    print_product(16)
    delete_product(16)
    print_all_products()
    print_filtered_products()
    search_products_by_name('ЗУБНАЯ')
