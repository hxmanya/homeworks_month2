import sqlite3

db_name = '''hw_8.db'''
try:
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT cities.id, cities.title 
                  FROM cities 
                  ORDER BY cities.title''')
        cities = cur.fetchall()


        while True:
            print("Вы можете отобразить список учеников по выбранному id города "
                  "из перечня городов ниже, для выхода из программы введите 0:")
            i = 1
            for city in cities:
                print(f"{i}. {city[1]}")
                i += 1

            try:
                choice = int(input("\nВведите ID города (0 для выхода): "))
                if choice == 0:
                    break

                if choice < 0 or choice > len(cities):
                    print("Неверный ID города. Пожалуйста, попробуйте снова.")
                    continue

                city_id = cities[choice - 1][0]

                # Получаем информацию об учениках выбранного города
                cur.execute('''
                    SELECT 
                        students.first_name,
                        students.last_name,
                        countries.title,
                        cities.title,
                        cities.area
                    FROM students
                    JOIN cities ON students.city_id = cities.id
                    JOIN countries ON cities.country_id = countries.id
                    WHERE cities.id = ?
                ''', (city_id,))

                students = cur.fetchall()

                if not students:
                    print("\nВ этом городе нет учеников.")
                else:
                    print("\nСписок учеников:")
                    for student in students:
                        print(f"Имя: {student[0]}")
                        print(f"Фамилия: {student[1]}")
                        print(f"Страна: {student[2]}")
                        print(f"Город проживания: {student[3]}")
                        print(f"Площадь города: {student[4]} кв. км")
                        print("-" * 50)

            except ValueError:
                print("Пожалуйста, введите число.")

except sqlite3.Error as error:
    print(error)

