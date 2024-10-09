
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marriage_status = "married" if self.is_married else "single"
        print(f'FULL NAME: {self.full_name}, AGE: {self.age}, '
              f'MARITAL STATUS: {marriage_status}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def get_marks(self):
        print("MARKS:")
        for key, value in self.marks.items():
            print(f'{key}: {value}')

    def average_mark(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def salary(self):
        final_salary = self.base_salary
        use_exp = self.experience
        while 3 < use_exp:
            final_salary += final_salary * 0.05
            use_exp -= 1
        print(f"{self.full_name} teacher's salary: {round(final_salary, 2)} som")

# Функция create_students через ввод в консоли
# def create_students():
#     students = []
#     for i in range(0, 3):
#         marks = {}
#         full_name = input("Enter Full Name of a student: ").title()
#         while True:
#             try:
#                 age = int(input("Enter Age of a student: "))
#             except ValueError:
#                 print("Enter an integer.")
#             else:
#                 break
#         while True:
#             try:
#                 is_married = input("Student is married?(yes/no): ")
#                 if is_married.upper() == 'YES':
#                     is_married = True
#                     break
#                 elif is_married.upper() == 'NO':
#                     is_married = False
#                     break
#                 else:
#                     raise ValueError
#             except ValueError:
#                 print("Enter only yes or no.")
#         try:
#             subject_counter = int(input("Enter number of subjects: "))
#         except ValueError:
#             print("Enter an integer.")
#             subject_counter = int(input("Enter number of subjects: "))
#         for i in range(subject_counter):
#             school_subject = input("Enter a school subject: ")
#             while True:
#                 try:
#                     subject_mark = int(input("Enter a mark: "))
#                 except ValueError:
#                     print("Enter an integer.")
#                 else:
#                     break
#             marks[school_subject] = subject_mark
#         one_student = Student(full_name, age, is_married, marks)
#         students.append(one_student)
#     return students

def create_students():
    students = [
        Student("Esenaliev Aman", 18, False, {"Math": 5, "Physics": 4, "History": 5}),
        Student("Petrov Vanya", 19, False, {"Math": 4, "Physics": 4, "History": 5}),
        Student("Koshonov Marat", 21, True, {"Math": 3, "Physics": 3, "History": 4})
    ]
    return students

teacher = Teacher('Aleksey Sensei', 35, True, 10)
teacher.introduce_myself()
print(f"{teacher.full_name} teacher's experience: {teacher.experience} years")
teacher.salary()


three_students = create_students()
for student in three_students:
    student.introduce_myself()
    student.get_marks()
    print(f"Average mark of student {student.full_name}: {student.average_mark()}")