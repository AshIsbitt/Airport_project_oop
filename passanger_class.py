# Passenger class
# inherits from people

# attributes:
# passport number

from people_class import *

class Passenger(People):
    def __init__(self, name, passport_id):
        super().__init__(name)
        self.__passport_id = passport_id

    def get_passport_id(self):
        return self.__passport_id

