# Assignment 1: Design Your Own Class - Superhero and Villain

# Base Class: Superhero
class Superhero:
    def __init__(self, name, power, strength_level):
        # Constructor to initialize superhero attributes
        self.name = name
        self.power = power
        self._strength_level = strength_level  # Encapsulated attribute (protected by convention)

    def use_power(self):
        # Method to simulate using a power
        return f"{self.name} uses {self.power}!"

    def display_info(self):
        # Method to display superhero information
        return (
            f"Name: {self.name}\n"
            f"Power: {self.power}\n"
            f"Strength Level: {self._strength_level}"
        )

    def get_strength_level(self):
        # Getter method for strength level
        return self._strength_level

    def set_strength_level(self, new_level):
        # Setter method with validation for strength level
        if 0 <= new_level <= 100:
            self._strength_level = new_level
        else:
            print("Invalid strength level. Must be between 0 and 100.")


# Subclass: Villain (inherits from Superhero)
class Villain(Superhero):
    def __init__(self, name, power, strength_level, evil_plan):
        # Call the base class constructor
        super().__init__(name, power, strength_level)
        self.evil_plan = evil_plan

    def use_power(self):
        # Overriding use_power method to show polymorphism
        return f"{self.name} uses {self.power} for evil! 💀"

    def reveal_evil_plan(self):
        # Method to reveal the villain's plan
        return f"{self.name}'s evil plan: {self.evil_plan}"


# --------- Example Usage ---------

# Create a superhero instance
hero = Superhero("SolarFlare", "Solar Blast", 85)

# Create a villain instance
villain = Villain("DarkMatter", "Black Hole Punch", 90, "Steal all the sunlight!")

# Use powers
print(hero.use_power())
print(villain.use_power())

# Display info
print("\n--- Hero Info ---")
print(hero.display_info())

print("\n--- Villain Info ---")
print(villain.reveal_evil_plan())

# Encapsulation in action
print("\n--- Updating Villain's Strength Level ---")
villain.set_strength_level(110)  # Invalid update
villain.set_strength_level(95)   # Valid update
print(f"Updated Strength Level: {villain.get_strength_level()}")
