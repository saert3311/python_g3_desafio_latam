from django.test import TestCase

# Create your tests here.

from .services import *

class VehicleServiceTestCase(TestCase):
    def setUp(self):
        vehicle = create_vehicle('ABC123', 'Toyota', 'Corolla', 2020)
        driver = create_driver(123456789, 'Juan', 'Perez')
        accounting_record = create_accounting_record('2020-01-01', 10000, vehicle)

    def test_create_driver(self):
        driver = create_driver(123456789, 'Juan', 'Perez')
        self.assertIsNotNone(driver)
        self.assertEqual(driver.rut, 123456789)
        self.assertEqual(driver.fname, 'Juan')
        self.assertEqual(driver.lname, 'Perez')

    def test_create_vehicle(self):
        vehicle = create_vehicle('ABC123', 'Toyota', 'Corolla', 2020)
        self.assertIsNotNone(vehicle)
        self.assertEqual(vehicle.plate, 'ABC123')
        self.assertEqual(vehicle.brand, 'Toyota')
        self.assertEqual(vehicle.model, 'Corolla')
        self.assertEqual(vehicle.year, 2020)

    def test_create_accounting_record(self):
        vehicle = create_vehicle('DEF123', 'Toyota', 'Corolla', 2021)
        accounting_record = create_accounting_record('2020-01-01', 10000, vehicle)
        self.assertIsNotNone(accounting_record)
        self.assertEqual(accounting_record.buy_date, '2020-01-01')
        self.assertEqual(accounting_record.value, 10000)
        self.assertEqual(accounting_record.vehicle, vehicle)

    def test_disable_driver(self):
        driver = create_driver(987654321, 'Pedro', 'Perez')
        self.assertTrue(driver.is_active)
        driver = disable_driver(987654321)
        self.assertFalse(driver.is_active)

    def test_disable_vehicle(self):
        vehicle = create_vehicle('GHI123', 'Toyota', 'Corolla', 2021)
        self.assertTrue(vehicle.is_active)
        vehicle = disable_vehicle('GHI123')
        self.assertFalse(vehicle.is_active)

    def test_enable_driver(self):
        driver = enable_driver(123456789)
        self.assertTrue(driver.is_active)
    
    def test_enable_vehicle(self):
        vehicle = enable_vehicle('ABC123')
        self.assertTrue(vehicle.is_active)

    def test_get_vehicle(self):
        vehicle = get_vehicle('ABC123')
        self.assertIsNotNone(vehicle)
        self.assertEqual(vehicle.plate, 'ABC123')

    def test_get_driver(self):
        driver = get_driver(123456789)
        self.assertIsNotNone(driver)
        self.assertEqual(driver.rut, 123456789)

    def test_assign_driver_vehicle(self):
        vehicle = create_vehicle('GHI123', 'Toyota', 'Corolla', 2021)
        driver = create_driver(987654321, 'Pedro', 'Perez')
        asigned = assign_driver_vehicle(987654321, 'GHI123')
        self.assertEqual(asigned.vehicle.plate, vehicle.plate)

    def test_print_vehicles(self):
        print('\n------- Test----------')
        print_vehicles()