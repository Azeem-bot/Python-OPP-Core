'''In Python, abstraction is the process of hiding complex implementation details and
 showing only the essential features of an object. 

1. Abstract Base Class (ABC): A class that inherits from abc.ABC. 
   It cannot be instantiated directly and serves as a blueprint for other classes.
2. Abstract Method: A method declared in an abstract class using the @abstractmethod decorator.
   It has no implementation and must be overridden in any subclass.
3. Concrete Method: A fully implemented method within an abstract class. 
   Subclasses inherit this default behaviour directly.'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Must be implemented by all subclasses"""
        pass

    def description(self):
        """Concrete method: provides shared functionality"""
        return "This is a geometric shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Usage
# shape = Shape()      # This would raise a TypeError
circle = Circle(5)
print(circle.area())  
print(circle.description()) # Output: This is a geometric shape.
