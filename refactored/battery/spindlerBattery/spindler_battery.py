from battery import Battery

class SpindlerBattery(Battery):
  def __init__(self, last_service_date, current_date):
    self._last_service_date = last_service_date
    self._current_date = current_date

  def needs_service(self):
    return False