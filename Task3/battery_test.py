from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery
import unittest
import datetime


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2004,4,1)
        current_date = datetime.datetime(2023, 1, 10)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2021,1,10)
        current_date = datetime.datetime(2023, 1, 10)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2013,5,25)
        current_date = datetime.datetime(2023, 1, 10)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2015,5,12)
        current_date = datetime.datetime(2023, 1, 10)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
