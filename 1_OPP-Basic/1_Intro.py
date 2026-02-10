'''
Key Components of Object-Oriented Programming (OOP) in Python:

* Class: A blueprint or template for creating objects, defined using the class keyword.
* Object: A specific instance of a class, created to represent real-world entities.
* Attributes: Variables that hold data related to the object.
* Methods: Functions defined within a class that define the behaviors or actions an object can perform.
* Self: A reference to the current instance of the class, used to access variables and methods.
* __init__ Method: A special constructor method that automatically initializes a new object's attributes. 
'''
class Car:
    # Constructor to initialize instance attributes
    def __init__(self, make, model, year):
        self.make = make    # Attribute
        self.model = model  # Attribute
        self.year = year    # Attribute

    # Method to define behavior
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating Objects (Instances of the class)
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)

# Accessing methods
car1.display_info() # Output: 2022 Toyota Camry
car2.display_info() # Output: 2023 Honda Civic