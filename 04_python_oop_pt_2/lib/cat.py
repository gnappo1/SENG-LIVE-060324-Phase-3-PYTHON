# import ipdb

# 7. ✅. Create a subclass of Pet called Cat
# import Pet from lib.pet

from pet import Pet

# 7. ✅. Create a subclass of Pet called Cat

# import Pet from lib.pet
# "is a?"
class A: pass
class B: pass
class C: pass

class Cat(Pet, A, B, C):
    all = []
    # 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
    # additional parameter called indoor (Boolean)

    # Use super to pass the Pet parameters to the super class (DRY)

    # Add an indoor attribute

    def __init__(self, outdoor, **kwargs):
        super().__init__(**kwargs) #! kwargs is a dict
        self.outdoor = outdoor

    # 9. ✅. Create a method unique to the Cat subclass called talk which returns the string "Meow!"

    # def meow(self):
    #     pass

    # 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet
    def print_pet_details(self):
        print(
            f"""
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            outdoor:{self.outdoor}
        """
        )
# Add super().print_pet_details() and print the indoor attribute
# def print_pet_details(self):
#     pass

spidey = Cat(outdoor=True, name="Spidey", age=2, breed="persian", temperament="docile", owner="Matteo")
print('done')
