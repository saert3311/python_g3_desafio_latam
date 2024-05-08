from .models import *

def create_vehicle(plate, brand, model, year):
    vehicle = Vehicle(plate=plate, brand=brand, model=model, year=year)
    vehicle.save()
    return vehicle

def create_driver(rut, fname, lname):
    driver = Driver(rut=rut, fname=fname, lname=lname)
    driver.save()
    return driver

def create_accounting_record(buy_date, value, vehicle):
    if isinstance(vehicle, int):
        vehicle = Vehicle.objects.get(pk=vehicle)
    accounting_record = AccountingRecord(buy_date=buy_date, value=value, vehicle=vehicle)
    accounting_record.save()
    return accounting_record

#me puse creativo para no reescribir lo mismo 4 veces

def vehicle_operator(plate, **kwargs):
    '''
    Funcion para operar vehiculos, si no se pasa un 2do argumento, se busca el vehiculo con la patente entregada
    en caso contrario se cambia el estado del conductor a activo o inactivo (bool)
    '''
    try:
        vehicle = Vehicle.objects.get(plate=plate)
        if kwargs:
            vehicle.is_active = kwargs['is_active']
            vehicle.save()
        return vehicle
    except Vehicle.DoesNotExist:
        print(f'No se encontró un vehículo con patente {plate}')
        return False
    return vehicle

def driver_operator(rut, **kwargs):
    '''
    Funcion para operar conductores, si no se pasa un 2do argumento, se busca el conductor con el rut entregado
    en caso contrario se cambia el estado del conductor a activo o inactivo (bool) o se asigna un vehiculo (Vehicle)
    '''
    rut = str(rut).replace('.','').replace('-','')
    try:
        driver = Driver.objects.get(rut=rut)
        if kwargs:
            if 'is_active' in kwargs:
                driver.is_active = kwargs['is_active']
            elif 'vehicle' in kwargs:
                vehicle = vehicle_operator(kwargs['vehicle'])
                if not vehicle.is_active:
                    print(f'El vehículo {vehicle.plate} no está activo')
                    return False
                driver.vehicle = vehicle
            driver.save()
        return driver
    except Driver.DoesNotExist:
        print(f'No se encontró un conductor con RUT {rut}')
        return False
    return driver



def enable_driver(rut):
    return driver_operator(rut, is_active=True)

def disable_driver(rut):
    return driver_operator(rut, is_active=False)

def enable_vehicle(plate):
    return vehicle_operator(plate, is_active=True)

def disable_vehicle(plate):
    return vehicle_operator(plate, is_active=False)

def get_driver(rut):
    return driver_operator(rut)

def get_vehicle(plate):
    return vehicle_operator(plate)

def assign_driver_vehicle(rut, plate):
    return driver_operator(rut, vehicle=plate)

def print_vehicles():
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        print(vehicle.full_description)