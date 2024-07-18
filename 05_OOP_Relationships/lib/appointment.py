import datetime


class Appointment:
    all = []

    def __init__(
        self, reason_for_visit, date, doctor_instance, patient_instance
    ):  # dependency injection
        self.reason_for_visit = reason_for_visit
        self.date = date
        self.doctor = doctor_instance
        self.patient = patient_instance
        type(self).all.append(self)

    #! Association Property
    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, doctor_instance):
        from lib.doctor import Doctor

        if type(doctor_instance) == Doctor:
            self._doctor = doctor_instance
        else:
            raise TypeError("doctors must be of type Doctor")

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient_instance):
        from lib.patient import Patient

        if type(patient_instance) == Patient:
            self._patient = patient_instance
        else:
            raise TypeError("patients must be of type patient")

    def __repr__(self):
        """this method returns the official representation of the object"""
        return f"""
            Appointment:
                Reason: {self.reason_for_visit}
                Date: {self.date}
                Patient Name: {self.patient.name}
                Doctor Name: {self.doctor.name}
        """
