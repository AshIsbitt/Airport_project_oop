# do the simplest SIMPLEST

# switch board
from passenger_class import *
from plane_class import *
from flight_trip_class import *

passenger_list = []
plane_list = []
flight_list = []

def switchboard():

    while True:
        print("------------------------------------")
        print("1. Create a new flight")
        print("2. Add passenger")
        print("3. Add Plane")
        print("0. Quit")
        entry = input("> ")

        if entry == "1":
            origin = input("Enter origin of flight: ")
            dest = input("Set destination: ")
            num_of_passengers = input("How many passengers: ")
            plane = int(input("Enter plane ID: ")) - 1
            flight_list.append(Flight_Trip(origin, dest, num_of_passengers, plane_list[plane].get_plane_id()))
            print("New flight created")
        elif entry == "2":
            name = input("Enter name: ")
            passenger_list.append(Passenger(name, len(passenger_list) + 1))
            print("New passenger: " + passenger_list[-1].get_name())
        elif entry == "3":
            cargo = int(input("How much cargo can be stored? "))
            plane_list.append(Plane(cargo, len(plane_list) + 1))
            print("New plane: " + str(plane_list[-1].get_plane_id()))
        elif entry == "0":
            quit()

switchboard()
