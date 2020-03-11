#Flight Trip class

# origin
# Destination
# list of passengers
# plane number

# need some getters nd setter:

# as a user I can add a plane
# as a User I can add a destination
# As a user I can add a origin

# As a user I can add a Passenger to the list of passengers

class Flight_Trip:
    def __init__(self, origin="", destination="", list_of_passengers=[], plane_id=0):
        self.__origin = origin
        self.__destination = destination
        self.__list_of_passengers = list_of_passengers
        self.__plane_id = plane_id

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_list_of_passengers(self):
        return self.__list_of_passengers

    def get_plane_id(self):
        return self.__plane_id

    def set_plane(self, plane_id):
        self.__plane_id = plane_id

    def set_origin(self, origin):
        self.__origin = __origin

    def set_destination(self, dest):
        self.__destination = dest

    def set_passenger(self, passenger):
        self.__list_of_passengers.append(passenger)
