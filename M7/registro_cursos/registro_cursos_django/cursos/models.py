from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    rut = models.CharField(max_length=9, verbose_name='RUT', primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    updated_at = models.DateField(auto_now=True, verbose_name='Actualizado el')
    created_by  = models.CharField(max_length=50, verbose_name='Creado por')

    def __eq__(self, other):
        return self.rut == other.rut

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Address(models.Model):
    street = models.CharField(max_length=50, verbose_name='Calle')
    number = models.CharField(max_length=10, verbose_name='Número')
    dept = models.CharField(max_length=5, verbose_name='Departamento')
    commune = models.CharField(max_length=50, verbose_name='Comuna')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    region = models.CharField(max_length=50, verbose_name='Estado')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')

    def __str__(self):
        return f'{self.street} {self.number}, {self.region}'


class Teacher(models.Model):
    rut = models.CharField(max_length=9, verbose_name='RUT', primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado el', blank=True, null=True)
    updated_at = models.DateField(auto_now=True, verbose_name='Actualizado el')
    created_by  = models.CharField(max_length=50, verbose_name='Creado por')

    def __eq__(self, other):
        return self.rut == other.rut

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    code = models.CharField(max_length=10, verbose_name='Código', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    version = models.IntegerField(verbose_name='Versión')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Profesor', blank=True, null=True)

    def __eq__(self, other):
        return self.code == other.code
 
    def __str__(self):
        return f'{self.name}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Estudiante')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateField(auto_now=True, verbose_name='Actualizado el')
    created_by  = models.CharField(max_length=50, verbose_name='Creado por')

    def __str__(self):
        return f'{self.student} - {self.course}'