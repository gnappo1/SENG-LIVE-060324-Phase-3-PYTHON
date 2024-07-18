from datetime import datetime
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

    @classmethod
    def filter_past_two_appointments(cls):
        # figure out current date
        today_date = datetime.now().date()
        # capture all the appointments whose dates respect the condition
        # filtered_appts = []
        # for appt in cls.all:
        #     if today_date > datetime.strptime(appt.date, "%m/%d/%y").date():
        #         filtered_appts.append(appt)
        # return filtered_appts
        filtered_appointments =  [
            appt
            for appt in cls.all
            if today_date > datetime.strptime(appt.date, "%m/%d/%y").date()
        ]
        if sorted_list := sorted(filtered_appointments, key=lambda appt: appt.date, reverse=True):
            return len(sorted_list) > 1 and sorted_list[:2]

    @classmethod
    def future_appointments(cls):
        filtered_list = list(set(cls.all) - set(cls.filter_past_appointments()))
        return sorted(
            filtered_list,
            key=lambda appt: appt.date,
        )

    def __repr__(self):
        """this method returns the official representation of the object"""
        return f"""
            Appointment:
                Reason: {self.reason_for_visit}
                Date: {self.date}
                Patient Name: {self.patient.name}
                Doctor Name: {self.doctor.name}
        """
