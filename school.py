class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return  f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {Lecturer.average_score(self)} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    def __lt__(self,other):
        if not isinstance(other,Student):
            return f"{other.name} не является студентом"
        return Lecturer.average_score(self) < Lecturer.average_score(other)
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_score(self):
        average_grades_per_course = []
        for course,grades in self.grades.items():
            average_grades_per_course += [(sum(grades) / len(grades))]
        average_grade = round((sum(average_grades_per_course) / len(average_grades_per_course)),1)
        return average_grade
    def __str__(self):
        return  f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_score()}"
    def __lt__(self, other):
        if not isinstance(other,Lecturer):
            return f"{other.name} не является лектором"
        return self.average_score() < other.average_score()
        



class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Harry', 'Potter', 'male')
best_student.courses_in_progress += ['Python','Go']
best_student.finished_courses += ['Java','LISP']

worst_student = Student('Drako', 'Malfoy', 'male')
worst_student.courses_in_progress += ['Java','LISP','Python']
worst_student.finished_courses += ['Go']
 
some_reviewer = Reviewer('Albus', 'Dumbledor')
some_reviewer.courses_attached += ['Python','Go']
 
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Go', 8)
some_reviewer.rate_hw(best_student, 'Go', 7)

other_reviewer = Reviewer('Nicolas', 'Flamel')
other_reviewer.courses_attached += ['Java','LISP','Python']

other_reviewer.rate_hw(worst_student,'LISP',9)
other_reviewer.rate_hw(worst_student,'LISP',7)
other_reviewer.rate_hw(worst_student,'Java',3)
other_reviewer.rate_hw(worst_student,'Java',2)
other_reviewer.rate_hw(worst_student,'Java',6)
other_reviewer.rate_hw(worst_student,'Python',2)
other_reviewer.rate_hw(worst_student,'Python',6)


some_lecturer = Lecturer('Severus', 'Snape')
some_lecturer.courses_attached += ['Python','Go']

other_lecturer = Lecturer('Minerva', 'McGonnagal')
other_lecturer.courses_attached += ['Java','LISP','Python']

best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Python', 7)
best_student.rate_lecture(some_lecturer, 'Python', 6)
best_student.rate_lecture(some_lecturer, 'Go', 8)
best_student.rate_lecture(some_lecturer, 'Go', 9)

worst_student.rate_lecture(other_lecturer,'LISP',1)
worst_student.rate_lecture(other_lecturer,'LISP',2)
worst_student.rate_lecture(other_lecturer,'LISP',4)
worst_student.rate_lecture(other_lecturer,'Java',6)
worst_student.rate_lecture(other_lecturer,'Java',7)
worst_student.rate_lecture(other_lecturer,'Python',7)
worst_student.rate_lecture(other_lecturer,'Python',7)

 
# print(best_student)
# print(worst_student)
# print(worst_student < best_student)
# print(best_student < some_reviewer)
# print(some_reviewer)
# print(other_reviewer)
# print(some_lecturer)
# print(other_lecturer)
# print(some_lecturer > other_lecturer)

def course_average_grade(gradees: list,course_name: str):
    avg_per_person = []
    for gradee in gradees:
        avg_per_person += [(sum(gradee.grades[course_name]) / len(gradee.grades[course_name]))]
    return round(sum(avg_per_course) / len(avg_per_course), 1)
#добавить проверку учится ли на курсе, является ли студентом, есть ли оценки


print(course_average_grade([best_student,worst_student], 'Python'))
print(course_average_grade([some_lecturer,other_lecturer], 'Python'))