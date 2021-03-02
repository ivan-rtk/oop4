class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.meanf = 0

    def sumgardS(self):
        count = 0
        sum_grades = 0
        list_grades = self.grades.values()
        for i in list_grades:
            count += len(i)
            sum_grades += sum(i)
            #print(count)
            #print(sum_grades)
            #print(i)
        self.meanf = round(sum_grades/count, 2)

    def __str__(self):
        self.sumgardS()
        return f"Имя:{self.name}\n" \
        f"Фамилия: {self.surname}\n" \
        f"Средняя оценка за домашние задания: {self.meanf}\n" \
        f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
        f"Завершенные курсы: Введение в програмирование {self.finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('t')
            return
        print(self.meanf)
        print(other.meanf)
        self.sumgardS()
        other.sumgardS()
        print(self.meanf)
        print(other.meanf)
        return self.meanf < other.meanf

    def student_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.gradesLecturer:
                lecturer.gradesLecturer[course] += [grade]
            else:
                lecturer.gradesLecturer[course] = [grade]
        else:
            print("ошибка student_grade ", lecturer.name, course, grade)
            return 'ошибка'

    def sumGardsStudent(self, spisokS, coursS):
        itog =0
        #print(len(spisokS))
        #print(spisokS[0])
        #print(coursS)
        c = 0
        for i in spisokS:
            try:
                a = i.grades[coursS]
                a_sum = sum(a)
                a_s_l = a_sum/len(a)
                #print(a)
                #print(a_sum)
                #print(a_s_l)
                itog += a_s_l
                c += 1
            except Exception:
                print('нет оценок у ', i.name)
        #print(itog/len(spisokS))
        return round(itog/c, 2)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.gradesLecturer = {}
        self.meanL =0

    def summeanL(self):
        countL = 0
        sum_gradesL = 0
        list_grades = self.gradesLecturer.values()
        #print(self.gradesLecturer)
        #print(list_grades)
        for i in list_grades:
            countL += len(i)
            sum_gradesL += sum(i)
            #print(countL)
            #print(sum_gradesL)
            #print(i)
        self.meanL = round(sum_gradesL / countL, 2)

    def __str__(self):
        self.summeanL()
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка:{self.meanL}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('error lt')
            return
        #print(self.meanL)
        #print(other.meanL)
        self.summeanL()
        other.summeanL()
        #print(self.meanL)
        #print(other.meanL)
        return (self.meanL) < (other.meanL)

    def sumGardsLecturers(self, listL, coursL):
        #print(len(listL))
        #print(listL[0])
        #print(coursL)
        itog =0
        cL = 0
        for i in listL:
            try:
                a = i.gradesLecturer[coursL]
                a_sum = sum(a)
                a_s_l = a_sum/len(a)
                #print(a)
                #print(a_sum)
                #print(a_s_l)
                itog += a_s_l
                cL += 1
            except Exception:
                print('нет оценок у ', i.name)
        #print(itog/len(listL))
        return round(itog/cL, 2)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return \
            f"Имя: {self.name}\n" \
            f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("ошибка", student.name, course, grade)
            return 'Ошибка'











student1 = Student('pit', 'ivanov', 'male')
student2 = Student('lisa', 'ivanova', 'female')
student3 = Student('lena', 'ivaskina', 'female')

lecturer1 = Lecturer('vasya', 'pupkin')
lecturer2 = Lecturer('sasha', 'pupkina')
lecturer3 = Lecturer('alena', 'pukina')

reviewer1 = Reviewer('aleg', 'ivanov')
reviewer2 = Reviewer('olga', 'ivanova')
reviewer3 = Reviewer('olga', 'vlasova')

student1.courses_in_progress += ['c++', 'go']
student2.courses_in_progress += ['java', 'c++']
student3.courses_in_progress += ['c++', 'go']

lecturer1.courses_attached += ['c++', 'go']
lecturer2.courses_attached += ['c++', 'java']
lecturer3.courses_attached += ['c++', 'go']

reviewer1.courses_attached += ['c++', 'go']
reviewer2.courses_attached += ['java']
reviewer3.courses_attached += ['c++', 'go']

# test = Lecturer('imfghdk', 'tyr')
# test.courses_attached += ['Python', 'java']
student1.student_grade(lecturer1, 'c++', 8.5)
student1.student_grade(lecturer1, 'c++', 6.0)
student1.student_grade(lecturer2, 'c++', 9.1)
student1.student_grade(lecturer2, 'c++', 9.6)
student1.student_grade(lecturer1, 'go', 9.1)
student1.student_grade(lecturer1, 'go', 6.3)
#student1.student_grade(lecturer3, 'c++', 5.5)
reviewer1.rate_hw(student1, 'c++', 9.3)
reviewer2.rate_hw(student2, 'java', 5.5)
reviewer2.rate_hw(student2, 'java', 9.5)
reviewer1.rate_hw(student1, 'c++', 6.5)
reviewer1.rate_hw(student2, 'c++', 7.5)
reviewer1.rate_hw(student2, 'c++', 8.5)
#reviewer1.rate_hw(student3, 'c++', 9.5)
#reviewer1.rate_hw(student3, 'c++', 10)
#print(test.name, test.surname, test.courses_attached)
#print(student1.name, student1.surname, student1.courses_in_progress)
#print(student1.name, student1.grades)
#print(lecturer1.name, lecturer1.gradesLecturer)
#print(reviewer1)
#print(lecturer1)
#print(student1)
#print(student1)
#print(student2)
#print(student1 < student2)

listLect = [lecturer2, lecturer1, lecturer3]
print(lecturer1.sumGardsLecturers(listLect,'c++'))
listStud = [student1, student2, student3]
print('-----------')
print(student1.sumGardsStudent(listStud,'c++'))