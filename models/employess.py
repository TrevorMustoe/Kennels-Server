class Employees():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, location_id, address):
        self.id = id
        self.name = name
        self.location = location_id
        self.address = address
      
