class School:

    def __init__(self) -> None:
        self.courses = []
        self.students = []

    def search_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def add_courses(self, course):
        if not course in self.courses:
            self.courses.append(course)
            return True
        return False

    def add_student(self, student):
        if not student in self.students:
            self.students.append(student)
            return True
        return False


class Course:

    def __init__(self, course_id, course_name, monthly_price, duration, discount) -> None:
        self.course_id = course_id
        self.course_name = course_name
        self.monthly_price = float(monthly_price)
        self.duration = duration
        self.discount = discount

    def calc_full_payment(self):
        sub_total_price = self.monthly_price * self.duration
        discount_value = sub_total_price * (self.discount / 100)

        return sub_total_price - discount_value


class Student:

    def __init__(self, student_id, student_name, course_id) -> None:
        self.student_id = student_id
        self.student_name = student_name
        self.course_id = course_id


unad_school = School()

# Cursos:
programacion = Course('C1', "Programación", 300000, 6, 20)
diseno_grafico = Course('C2', "Diseño Gráfico", 250000, 4, 15)
redes = Course('C3', "Redes", 200000, 5, 10)

# Añadiendo los cursos:
unad_school.add_courses(programacion)
unad_school.add_courses(diseno_grafico)
unad_school.add_courses(redes)

# Estudiantes:
daniel = Student('E1', 'Daniel', 'C1')
sofia = Student('E2', 'Daniel', 'C2')
pedro = Student('E3', 'Pedro', 'C3')
