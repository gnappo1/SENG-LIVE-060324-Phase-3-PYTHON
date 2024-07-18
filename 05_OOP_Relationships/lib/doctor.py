from .appointment import *


class Doctor:
    all = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
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
    def field(self):
        return self._field

    @field.setter
    def field(self, new_field):
        if not isinstance(new_field, str):
            raise TypeError("field must be of type string")
        elif not new_field:
            raise ValueError("fields must be at least one char long")
        else:
            self._field = new_field

    #! Association Methods
    def appointments(self): # direct association
        from lib.appointment import Appointment
        return [appt for appt in Appointment.all if appt.doctor is self]

    def patients(self): # through association
        return list({appt.patient for appt in self.appointments()})
