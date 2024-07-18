from lib.pet import Pet

class Owner:
    all = [] #! memoization strategy

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        type(self).all.append(self)

    def pets(self):
        # final_list = []
        # for pet_instance in Pet.all:
        #     if pet_instance.owner is self:
        #         final_list.append(pet_instance)
        # return final_list
        return [pet_instance for pet_instance in Pet.all if pet_instance.owner is self]
