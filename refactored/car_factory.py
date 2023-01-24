
from car import Car


class CarFactory:
  def create_calliope(self, current_date, service_date, current_mileage, last_service_mileage):
    return Car(current_date, service_date, current_mileage, last_service_mileage)

  def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(current_date, last_service_date, current_mileage, last_service_mileage)

  def create_palindrome(self, current_date, last_service_date, warning_light_on):
    return Car(current_date, last_service_date, warning_light_on)

  def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(current_date, last_service_date, current_mileage, last_service_mileage)

  def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
    return Car(current_date, last_service_date, current_mileage, last_service_mileage)