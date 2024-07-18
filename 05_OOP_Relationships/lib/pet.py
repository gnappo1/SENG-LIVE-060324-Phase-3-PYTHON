class Pet:
    all = []

    def __init__(self, name, breed, owner_instance):
        self.name = name
        self.breed = breed
        self.owner = owner_instance  #! respecting SSoT
        type(self).all.append(self)

    #! Properties
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be of type string")
        elif not new_name:
            raise ValueError("Names must be at least one char long")
        else:
            self._name = new_name

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        if not isinstance(new_breed, str):
            raise TypeError("Breed must be of type string")
        elif not new_breed:
            raise ValueError("Breeds must be at least one char long")
        else:
            self._breed = new_breed

    #! Association Property
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner_instance):
        from lib.owner import Owner
        if type(owner_instance) == Owner:
            self._owner = owner_instance
        else:
            raise TypeError("Owners must be of type Owner")

    def __repr__(self):
        """this method returns the official representation of the object"""
        return f"""
            Pet:
                Name: {self.name}
                Breed: {self.breed}
        """
