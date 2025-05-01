# Activity 2: Polymorphism Challenge - Vehicles

# Base class
class Vehicle:
    def move(self):
        # This method will be overridden by each subclass
        raise NotImplementedError("Subclasses must implement this method.")


# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"


# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling along the path 🚴"


# --------- Example Usage ---------

# List of different vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

print("Vehicle Movements:\n")
for v in vehicles:
    # Polymorphism in action: same method name, different behavior
    print(v.move())
