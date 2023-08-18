class Vehicle:
    def __init__(self):
        raise NotImplementedError("Do not create Vehicle objects.")


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.name = "Car"

    def __str__(self):
        return self.name


class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2
        self.name = "Motorcycle"

    def __str__(self):
        return self.name


print(Car())
print(Motorcycle())
Vehicle()
