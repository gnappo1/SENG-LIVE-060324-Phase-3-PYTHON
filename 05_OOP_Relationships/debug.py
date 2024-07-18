#!/usr/bin/env python3

from lib.pet import Pet
from lib.owner import Owner


# pat = Owner(
#     "Pat",
#     "Jones",
# )
# rose = Owner(
#     "Rose",
#     "Smith",
# )

# taco = Pet(
#     "Taco",
#     "Cat",
#     pat
# )
# fido = Pet(
#     "Fido",
#     "Dog",
#     pat
# )
# princess = Pet(
#     "Princess",
#     "Fish",
#     rose
# )

# joe = Owner("Joe", "Jones")
# theresa = Owner("Theresa", "Jones")


from lib.appointment import Appointment
from lib.doctor import Doctor
from lib.patient import Patient

jimmy = Patient("Jimmy")
patty = Patient("Patty")
may = Patient("May")

rosenbaum = Doctor("Dr. Rosenbaum", "Gynocology")
williams = Doctor("Dr. Williams", "Oncology")


a1 = Appointment("Stomach issues.", "5/25/23", rosenbaum, may)
a2 = Appointment(
    "Non-stop migrains",
    "5/26/23",
    rosenbaum,
    patty,
)
a3 = Appointment(
    "Legs always sore in the mornings",
    "5/23/23",
    williams,
    jimmy,
)
a4 = Appointment(
    "Feels light-headed when jogging",
    "5/12/24",
    williams,
    patty,
)
a5 = Appointment("Can't keep food down", "8/30/24", rosenbaum, may)


import ipdb

ipdb.set_trace()
