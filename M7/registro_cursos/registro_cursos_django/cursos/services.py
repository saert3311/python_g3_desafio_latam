from .models import *

#teoricamente el created_by deberia ser el usuario logeado, pero para efectos de este ejercicio se dejara como 'Service'

def create_student(rut, first_name, last_name, birth_date):
    student = Student(rut=rut, first_name=first_name, last_name=last_name, birth_date=birth_date, created_by='Service')
    student.save()
    return student

def create_teacher(rut, first_name, last_name):
    teacher = Teacher(rut=rut, first_name=first_name, last_name=last_name, created_by='Service')
    teacher.save()
    return teacher

def create_address(street, number, dept, commune, city, region, student):
    if isinstance(student, int):
        student = Student.objects.get(pk=student)
    address = Address(street=street, number=number, dept=dept, commune=commune, city=city, region=region, student=student)
    address.save()
    return address

def create_course(code, name, version):
    course = Course(code=code, name=name, version=version)
    course.save()
    return course

def get_teacher(rut):
    return Teacher.objects.get(pk=rut)

def get_course(code):
    return Course.objects.get(pk=code)

def get_student(rut):
    return Student.objects.get(pk=rut)

def create_enrollment(student, course):
    if isinstance(student, int):
        student = Student.objects.get(pk=student)
    if isinstance(course, int):
        course = Course.objects.get(pk=course)
    enrollment = Enrollment(student=student, course=course, created_by='Service')
    enrollment.save()
    return enrollment

def assign_teacher(course, teacher):
    if isinstance(course, int):
        course = Course.objects.get(pk=course)
    if isinstance(teacher, int):
        teacher = Teacher.objects.get(pk=teacher)
    course.teacher = teacher
    course.save()
    return course

def print_student_enrollments(rut):
    student = Student.objects.get(pk=rut)
    enrollments = Enrollment.objects.filter(student=student)
    print(f'Cursos inscritos para {student.first_name} {student.last_name}:')
    for enrollment in enrollments:
        print(f'{enrollment.course}')