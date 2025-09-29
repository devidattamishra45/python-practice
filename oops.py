class Dog :
     species="canis familirs"
     def __init__(self, name , breed):
          self.name=name
          self.breed=breed

     def bark(self):
      print(f"{self.name}says Woof!")

s1=Dog("sachin",18)
print(s1.name)
class Student:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
       return f"Student nmae:{self.name}"
    def __repr__(self):
        return f"Student('{self.name}')"
    def  _len_(self):
        return len(self.name)

s = Student("Sachin")   # __init__ is called
print(s.name)
print(s)
print(repr(s))
 
class Dog:  # We define a class called "Dog"
    species = "Canis familiaris" # A class attribute (shared by all Dogs)

    def __init__(self, name, breed):  # The constructor (explained later)
        self.name = name     # An instance attribute to store the dog's name
        self.breed = breed   # An instance attribute to store the dog's breed

    def bark(self):          # A method (an action the dog can do)
        print(f"{self.name} says Woof!")

# Now, let's create some Dog objects:
my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object called my_dog
another_dog = Dog("Lucy", "Labrador")     # Creating another object

# We can access their attributes:
print(my_dog.name)       # Output: Buddy
print(another_dog.breed)  # Output: Labrador

# And make them perform actions:
my_dog.bark()            # Output: Buddy says Woof!
print(Dog.species)       # Output: Canis familiaris
#consturutor

class Empoyee:
    def __init__(self,name, salary,bond):
        self.name=name
        self.salary=salary
        self.bond=bond

    def get_salary(self):
        return self.salary  

e1=Empoyee("sachin",34000,4)
class Dog:
    def __init__(self, name, breed):  # The constructor
        self.name = name      # Setting the name attribute
        self.breed = breed    # Setting the breed attribute

# When we do this:
my_dog = Dog("Fido", "Poodle")  # The __init__ method is automatically called

class Animal:  # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self):  # We *override* the speak method (more on this later)
        print("Woof!")

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)  # Output: Rover
print(my_cat.name)  # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  # Output: Woof!
my_cat.speak()  # Output: Meow!
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        #  'other' refers to the object on the *right* side of the +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self): # String representation (for print() and str())
        return f"({self.x}, {self.y})"

    def __eq__(self, other): # Overloading == operator
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)
print(p3)      # Output: (4, 6)  (This uses the __str__ method)

print(p1 == p2) # Output: False (This uses the __eq__ method)