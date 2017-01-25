class User:

    def __init__ (self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password


class Student(User):

    student_list = []

    def __init__(self, name, mail, password):
        User.__init__(self, name, mail, password)
        self.grade_list = []
        self.attendance_list = []
        self.submission_list = []

    @classmethod
    def add_student(cls, name, mail, password):
        cls.student_list.append(Student(name, mail, password))

    @classmethod
    def edit_student(cls, name):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def remove_student(cls, name):
        for student in cls.student_list:
            if student.name == name:
                cls.student_list.remove(student)

    @classmethod
    def get_student_list(cls):
        return cls.student_list

    @classmethod
    def get_student(cls, name):
        for student in cls.student_list:
            if student.name == name:
                return student

    @classmethod
    def get_grade(cls, name, assignment_title):
        for student in cls.student_list:
            if student.name == name:
                for submission in student.submission_list:
                    if submission.title == assignment_title:
                        return submission.grade
                    else:
                        print('there is no such submission added by {}'.format(student.name))
            else:
                print('there is no such student in students list')

class Employee(User):
    pass


class Mentor(Employee):

    mentor_list = []

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)

    @classmethod
    def add_mentor(cls, name, mail, password):
        cls.mentor_list.append(Mentor(name, mail, password))

    def edit_mentor(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def remove_mentor(cls, mentor):
        cls.mentor_list.remove(mentor)

    @classmethod
    def get_list_mentor(cls):
        return cls.mentor_list


class Boss(Employee):

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)


class Staff(Employee):

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)