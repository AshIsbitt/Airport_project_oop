# define plane class
# it inherits from aircraft

# attributes it needs:
    # plane_number

from aircraft_class import *

class Plane(Aircraft):
    def __init__(self, cargo, plane_id):
        super().__init__(cargo)
        self.__plane_id = plane_id

    def get_plane_id(self):
        return self.__plane_id
