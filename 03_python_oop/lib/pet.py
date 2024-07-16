# !/usr/bin/env python3
# Defines the location of the Python interpreter
# See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes
#! useful functions and properties
# vars(obj_name_here) -> instance variables/attributes
# dir(obj_name_here) -> all members
# type(obj_name_here) -> what class does the object belong to
# obj_name_here.__class__ -> what class does the object belong to
# issubclass(classA, classB) -> who is the base and who is the derived class
# isinstance(object_name, class_name) -> is the class on the right the belonging class of the obj on the left
# 1. ✅ Create a Pet class

# __name__ -> dunder method/ special built-in methods leveraged under the hook
# __name > name mangling used for "privacy"
# _name -> for protected attributes when you set up properties
# name_ -> leveraged when you want to use reserved keywords
class Pet:
    #! every time we do Pet() 2 methods are invoked:
    # 1. new -> class method that allocates memory space, instantiate the object and then passes the newly instantiated object to the __init__
    # 2. __init__ -> instance method (birth of an object) that receives the newly created instance as SELF and it let you do whatever you want with it
    def __init__(self, name, breed, age=0):
        self.name = name #! please use the property setter name= to decide if the name given is valid
        self.breed = breed
        self.age  = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise AttributeError("Names must be of type string")
        elif not len(name):
            raise AttributeError("Names must be at least one character long")
        self._name = name #! set the property manually if we bypassed validations

    name = property(get_name, set_name)

    def __repr__(self): #! override the official object representation
        return f"""
        <Pet: {self.name} - 
            breed: {self.breed},
            age: {self.age}        
            /> """

    def __str__(self): #! override the unofficial object representation
        return f"""
        <Pet: {self.name}: 
            breed: {self.breed},
            /> """

    def speak(self): #! instance method, aka method for every object inside the class
        return "Ciao!"

fido = Pet(breed="pug", name="Fido", age=2)
milo = Pet(name="Milo", breed="husky", age=5)
# milo.print_details()
ipdb.set_trace()
# Note: Add 'pass' to the Pet class

# 2. ✅ Instantiate a few Pet instances

# Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__

# Add arguments to instances

# Attributes:
# name
# age
# breed
# temperament
# owner

# Use dot notation to access each Pet instance's attributes

# Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's
# attributes

# Review the "self" keyword

# Invoke "print_pet_details" on an instance

# Example Terminal Ouput:
# name: Rose
# age: 11
# breed: Domestic Longhair
# temperament: Sweet

# 5. ✅ Create an Owner class with two instance methods:

# get_name => Retrieve Owner's name

# set_name => Set Owner's name

# Ensure that Owner's name is a String

# If not, issue warning of "Name must be a string"

# Use property() to compile get_name / set_name and invoke them
# whenever we access an Owner instance's name

# Object Properties => Attributes that are controlled by methods
