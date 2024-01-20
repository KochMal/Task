class Student:
    def __init__(self, name, age, group, grades):
        self.name = name
        self.age = age
        self.group = group
        self.grades = grades

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

name = input("Введите имя студента: ")
age = int(input("Введите возраст студента: "))
group = input("Введите группу студента: ")

grades = []
num_grades = int(input("Введите количество оценок по литературе: "))
for i in range(num_grades):
    grade = float(input("Введите оценку №{}: ".format(i + 1)))
    grades.append(grade)

student = Student(name, age, group, grades)
average_grade = student.calculate_average_grade()

print("Средняя оценка студента {} из группы {} равна {}".format(student.name, student.group, average_grade))
