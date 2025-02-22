
from car import Car
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capuletEngine import CapuletEngine
from engine.sternmanEngine import SternmanEngine
from engine.willoughbyEngine import WilloughbyEngine


class CarFactory:
  @staticmethod
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(last_service_mileage, current_mileage)
    battery = SpindlerBattery(current_date, last_service_date)
    return Car(engine, battery)
    
  @staticmethod
  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


  @staticmethod
  def create_palindrome(current_date, last_service_date, warning_light_is_on):
    engine = SternmanEngine(warning_light_is_on)
    battery = SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)


  @staticmethod
  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    return Car(engine, battery)

  @staticmethod
  def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    return Car(engine, battery)