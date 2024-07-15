# Sequence Types

# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.
pet_names = [
    "Rose",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Luke",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
]

#! Lists
# TODO Creating Lists
# 1. ✅ Create a list of 10 pet names

# TODO Reading Information From Lists
# 2. ✅ Return the first pet name
# print(pet_names[0])
# print(pet_names[-1]) #! python allows negative indeces inside []
# 3. ✅ Return all pet names beginning from the 3rd index (included)
# print(pet_names[:]) #! ...
# print(pet_names[3:]) #! the end index is not specified so it goes until the end of the list
# 4. ✅ Return all pet names before the 3rd index (not included)
# print(pet_names[:3])
# 5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index alternating
# print(pet_names[3:8:2])
# 6. ✅ Find the index of a given element
# try:
#     id_ = pet_names.index("luke")
#     print(id_)
# except ValueError as e:
#     print(e)
# 7. ✅ Read the original list in reverse order
# pet_names.reverse() #! WATCH OUT: destructive method!!!!
# print(pet_names, pet_names[::-1]) #! PREFERRED WAY if you care about the integrity of the original DS
# 8. ✅ Return the frequency of a given element
# print(pet_names.count("Luke"))


# TODO Updating Lists
# 9. ✅ Change the first pet_name to all uppercase letters
# pet_names[0] = pet_names[0].upper()
# 10. ✅ Append a new name to the list
# pet_names.append("Fido")  #!append() takes exactly one argument
# 11. ✅ Add a new name at a specific index
# pet_names.insert(20, "Fido")  #!append() takes exactly two arguments: where (index), what (to insert)
# print(pet_names)
# 12. ✅ Add two lists together
# new_pet_names = ["Rover", "Fido"]
# final_list = pet_names + new_pet_names
# first, *rest = final_list
# print(pet_names + new_pet_names)
# 13. ✅ Remove the final element from the list
# pet_names.pop()
# 14. ✅ Remove element by specific index
# pet_names.pop(3) #! removed one element, the one in the position indicated
# 15. ✅ Remove a specific element
# pet_names.remove(
#     "Lea"
# )  #! removes the first occurrence from the list IF ANY, otherwise: ValueError: list.remove(x): x not in list
# 16. ✅ Remove all pet names from the list
# pet_names.clear() #! simply clears the content of the list, but the list still exists
# del pet_names #! deletes the variable/pointer and consequently memory will be cleared


#!Tuple
# 📚 Review:
# Mutable, Immutable <=> Changeable, Unchangeable

# Why Are Tuples Immutable?

# What advantages does this provide for us? In what situations
# would this serve us?
# TODO Accessing Elements
# 17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages
empty_tuple = ()
single_tuple = (True,)
ages_generator = tuple(range(10))


# 18. ✅ Print the first pet age

# TODO Testing Mutability (you can add a tuple to a tuple though)
# 19. ✅ Attempt to remove an element with ".pop"
# 20. ✅ Attempt to change the first element

#! YOU CAN MODIFY MUTABLE DATA STRUCTURES INSIDE A TUPLE

# TODO Tuple Methods
# 21. ✅ Return the frequency of a given element
#! COUNT
# ages_generator.count(2) #! counts all the occurrences of an element
# 22. ✅ Return the index of a given element
#! INDEX
# ages_generator.index(
#     2
# )  #! finds the first occurrence of an element, othewise: ValueError: tuple.index(x): x not in tuple

#! Range
# 23. ✅ create a Range
# Note:  Ranges are primarily used in loops
# r = range(5)
# #! count
# r.count(3)
# #! index
# r.index(4)
# #! step
# r.step
# #! stop
# r.stop
# #! start
# r.start

#! Sets (value cannot be modified but you can add/remove elements)
# 24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}
small_pet_fav_food = {'bacon'}

# TODO Reading
# 27. ✅ Print set elements with a loop
# for el in pet_fav_food:
#     print(el)
# 27. ✅ Check if an element is in a set
# print("fish" in pet_fav_food)
# 27. ✅ Get first element
# i = iter(pet_fav_food)
# next(i)
# 28. ✅ Get a copy of a set
# copied_set = pet_fav_food.copy()
# 28. ✅ isdisjoint, issubset, issuperset
# print(pet_fav_food.issuperset(small_pet_fav_food))
# print(pet_fav_food.issubset(small_pet_fav_food))
# print(pet_fav_food.isdisjoint(small_pet_fav_food))

# TODO Updating
# 29. ✅ Add an element to a set
# pet_fav_food.add("Tuna")
# 30. ✅ Union, intersection, difference
a = {1, 2, 3, 4}
b = {8, 9, 3, 4}
# a.intersection(b) #! {3, 4} NON DESTRUCTIVE
# a.union(b)  #! {1, 2, 3, 4, 8, 9} NON DESTRUCTIVE
# a.difference(b)  #! {1, 2} NON DESTRUCTIVE
# 30. ✅ Update current set with elements from other set
# a.difference_update(b)  #! {1, 2} DESTRUCTIVE!!!!!

# TODO Deleting
# 31. ✅ Delete specific el using ".remove"
pet_fav_food.remove(
    "yhwegvfiuwgfiug3"
)  #! it will remove the unique element if present, else KeyError
# 32. ✅ Delete random element using ".pop"
# 33. ✅ Delete the last item for Rose using "popitem()"
# 33b ✅ Delete every key/value pair


#! Dictionaries (from 3.7+, dictionaries are ordered)
# TODO Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# TODO Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
# print(pet_info_rose['names']) #! will retrieve the value if the key EXISTS, otherwise KeyError!
# 28. ✅ Print the pet attribute of "age" using ".get"
# print(pet_info_rose.get('names', "default value in case of absence"))

# Note: ".get" is preferred over bracket notation in most cases
# because it will return "None" instead of an error
# 28b. ✅ Get dict keys
# pet_info_rose.keys()
# # 28c. ✅ Get dict values
# pet_info_rose.values()
# # 28d. ✅ Get dict pairs
# pet_info_rose.items()

# TODO Updating
# 29. ✅ Update Rose's age to 12
# pet_info_rose["age"] +=1
# pet_info_rose["age"] = pet_info_rose["age"] + 1
# 30. ✅ Update Spot's age to 26
# pet_info_rose.update({"age": 26, "new": True})
# print(pet_info_rose)

pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
# TODO Deleting
# 31. ✅ Delete Rose's age using the "del" keyword => []
# del pet_info_rose['age']
# 32. ✅ Delete Spot's age using ".pop"
pet_info_rose.pop("ages")  #! removed the key/value pair if existing, else KeyError
print(pet_info_rose)
# 33. ✅ Delete the last item for Rose using "popitem()"
pet_info_rose.popitem()
# 33b ✅ Delete every key/value pair => clear()
pet_info_rose.clear()

#! Loops
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

# 34. ✅ Loop through a range of 10 and print every number within the range
# 35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# 36. ✅ Loop through the "pet_info" list and print every dictionary
# 37. ✅ Create a function that takes a list a parameter
# The function should use a "for" loop to loop through the list and print each item
# Invoke the function and pass it "pet_names" as an argument
# 38. ✅ Create a function that takes a list as a parameter
# The function should define a variable ("counter") and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Once the loop has finished, return the final value of "counter"

# 39. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dictionaries", "name" and "age" as parameters
# Create an index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param
# and the index is less then the length of the list
# Every list will increase the index by 1
# If the dictionary containing a matching name is found, update the item's age with the new age
# Otherwise, return 'Pet not found'

#! Functional Programming corner
# map like VS map
# 40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

# find like VS find
# 41. ✅ Use list comprehension to find a pet named spot

# filter like VS filter
# 42. ✅ Use list comprehension to find all of the pets under 3 years old

# reduce like VS reduce
# 42. ✅ Use list comprehension to find all of the pets under 3 years old

#! Writing Generators
# 43. ✅ Create a generator expression matching the filter above

#! Compare Generators and Expressions
import sys
import timeit
starter_list = list(range(100000))

#! MEMORY
print("List Comprehension Memory Size", sys.getsizeof([el for el in starter_list if el%2==0]))
# 444376
print("Generator Expression Memory Size",sys.getsizeof((el for el in starter_list if el%2==0)))
#208

#! RUNTIME
print("Comprehension Run 1 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1))
#=> 0.005183833185583353
print("Comprehension Run 1000 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1000))
# => 2.4483373747207224
print("Generator Run 1 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1))
# => 9.041279554367065e-06
print("Generator Run 1000 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1000))
# => 0.00024854158982634544
