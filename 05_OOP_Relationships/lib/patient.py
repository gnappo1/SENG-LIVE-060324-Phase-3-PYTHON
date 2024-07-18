from datetime import datetime
class Patient:
    all = []

    def __init__(self, name):
        self.name = name
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
        elif hasattr(self, 'name'):
            raise ValueError("Names cannot be reset after initialization")
        else:
            self._name = new_name

    #! Association Methods

    def appointments(self): # direct association
        from lib.appointment import Appointment
        return [appt for appt in Appointment.all if appt.patient is self]

    def doctors(self): # through association
        return list({appt.doctor for appt in self.appointments()})
