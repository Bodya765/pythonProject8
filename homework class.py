class SchoolMember:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
class Teacher(SchoolMember):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
    def tell(self):
        print(f"Вчитель: {self.first_name} {self.last_name}, Зарплата: {self.salary}")


class Student(SchoolMember):
    def __init__(self, first_name, last_name, grades):
        super().__init__(first_name, last_name)
        self.grades = grades

    def tell(self):
        average_grade = sum(self.grades) / len(self.grades)
        print(f"Учень: {self.first_name} {self.last_name}, Середній бал: {average_grade}")
teacher1 = Teacher("Іван", "Шевченко", 10000)
teacher2 = Teacher("Олена", "Ковальчук", 11500)
student1 = Student("Марія", "Сидоренко", [90, 85, 88])
student2 = Student("Олександр", "Коваль", [78, 82, 80])
teacher1.tell()
teacher2.tell()
student1.tell()
student2.tell()
