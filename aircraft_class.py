# aircraft class
# attributes: cargo


# Define a couple of methods, accelerate and break

class Aircraft:
    def __init__(self, cargo):
        self.__cargo = cargo

    #getter
    def get_cargo(self):
        return self.__cargo
