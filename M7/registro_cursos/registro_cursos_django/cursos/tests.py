from django.test import TestCase

from .services import *

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Jhon',
            last_name='Smith',
            rut='12345678-9',
            birth_date='1990-01-01'
        )
        self.address = Address.objects.create(
            street='Fake St.',
            number='123',
            dept='A',
            commune='Santiago',
            city='Santiago',
            region='RM',
            student=self.student
        )
        self.course = Course.objects.create(
            code='INF001',
            name='Programming',
            version='1'
        )
        self.teacher = Teacher.objects.create(
            first_name='Jane',
            last_name='Doe',
            rut='98765432-1'
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course
        )

    def test_create_student(self):
        student = create_student('12345678-9', 'John', 'Doe', '1990-01-01')
        self.assertEqual(student.first_name, 'John')
        self.assertEqual(student.last_name, 'Doe')
        self.assertEqual(student.rut, '12345678-9')
        self.assertEqual(student.birth_date, '1990-01-01')
    
    def test_create_teacher(self):
        teacher = create_teacher('98765432-1', 'Jane', 'Doe')
        self.assertEqual(teacher.first_name, 'Jane')
        self.assertEqual(teacher.last_name, 'Doe')
        self.assertEqual(teacher.rut, '98765432-1')
    
    def test_create_address(self):
        address = create_address('Fake St.', '123', 'A', 'Santiago', 'Santiago', 'RM', self.student)
        self.assertEqual(address.street, 'Fake St.')
        self.assertEqual(address.number, '123')
        self.assertEqual(address.dept, 'A')
        self.assertEqual(address.commune, 'Santiago')
        self.assertEqual(address.city, 'Santiago')
        self.assertEqual(address.region, 'RM')
        self.assertEqual(address.student, self.student)
    
    def test_get_student(self):
        student = get_student('12345678-9')
        self.assertEqual(student, self.student)
    
    def test_get_teacher(self):
        teacher = get_teacher('98765432-1')
        self.assertEqual(teacher, self.teacher)

    def test_get_course(self):
        course = get_course('INF001')
        self.assertEqual(course, self.course)

    def test_assign_teacher(self):
        course = assign_teacher(self.course, self.teacher)
        self.assertEqual(course.teacher, self.teacher)

    def test_create_enrollment(self):
        another_course = create_course('INF002', 'Programming II', 1)
        enrollment = create_enrollment(self.student, another_course)
        print_student_enrollments('12345678-9')
        self.assertEqual(enrollment.student, self.student)
        self.assertEqual(enrollment.course, another_course)
