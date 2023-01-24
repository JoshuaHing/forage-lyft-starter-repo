# import serviceable class
from serviceable import Serviceable

# import the engine class from the neighbouring engine folder
from engine.engine import Engine
from battery.battery import Battery



class Car(Serviceable):
  def __init__(self, engine: Engine, battery: Battery):
    self._engine = engine
    self._battery = battery

  # either engine or battery needs service..
  def needs_service(self):
    return self.engine.needs_service() or self.battery.needs_service()
  