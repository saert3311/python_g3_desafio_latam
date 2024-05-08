from django.db import models

# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=6, verbose_name='Patente', unique=True, primary_key=True)
    brand = models.CharField(max_length=50, verbose_name='Marca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    year = models.IntegerField(verbose_name='Año')
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    @property
    def full_description(self):
        return f'{self.plate}: {self.brand} {self.model} {self.year}'

    def __str__(self):
        return f'{self.model} {self.year}'

    def __eq__(self, other):
        try:
            return self.plate == other.plate
        except AttributeError:
            return False

class Driver(models.Model):
    rut = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='RUT')
    fname = models.CharField(max_length=50,  verbose_name='Nombre')
    lname = models.CharField(max_length=50,  verbose_name='Apellido')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    vehicle = models.OneToOneField (Vehicle, verbose_name='Vehículo', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

    def __eq__(self, other):
        try:
            return self.rut == other.rut
        except AttributeError:
            return False

class AccountingRecord(models.Model):
    buy_date = models.DateField(verbose_name='Fecha de compra')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    vehicle = models.OneToOneField(Vehicle, verbose_name='Vehículo', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle} {self.value}'