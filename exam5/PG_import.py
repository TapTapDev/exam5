
# =========================== Task 2 =======================================================

import faker
from dataclasses import dataclass
from exam5.faker_import_test import PG
f = faker.Faker()

@dataclass
class Department(PG):
    name: str = None
    head_id: int = None

def department_faker(count=0):
    counter = 0
    while counter < count:
        data = {
            "name": f.first_name(),
            "head_id": f.random_int(1,100)
        }
        Department(**data).save()
        counter += 1

# department_faker(10)

@dataclass
class Professor(PG):
    name: str = None
    department_id: int = None

def professors_faker(count=0):
    counter = 0
    while counter < count:
        data = {
            "name": f.first_name(),
            "department_id": f.random_int(1,100)
        }
        Professor(**data).save()
        counter += 1
# professors_faker(50)

@dataclass
class Student(PG):
    name: str = None
    groupp: int = None

def student_faker(count=0):
    counter = 0
    while counter < count:
        data = {
            "name": f.first_name(),
            "groupp": f.random_int(1,100)
        }
        Student(**data).save()
        counter += 1
# student_faker(500)

@dataclass
class Enrollment(PG):
    student_id: int = None
    professor_id: int = None
    course_name: str = None
    grade: int = None

def enrollment_faker(count=0):
    counter = 0
    while counter < count:
        data = {
            "student_id": f.random_int(1,100),
            "professor_id": f.random_int(1,50),
            "course_name": f.first_name(),
            "grade": f.random_int(1,100)
        }
        Enrollment(**data).save()
        counter += 1
# enrollment_faker(1000)




