class Patient:
    def __init__(self, name, age, medical_history, symptoms, prescribed_doctor, status="Under Treatment"):
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.symptoms = symptoms
        self.prescribed_doctor = prescribed_doctor
        self.status = status

    def get_status(self):
        status = "Under Treatment" if self.status == "Under Treatment" else "Recovered"
        if self.status == "Under Treatment":
            return f"Patient: {self.name}, Age: {self.age}, Status: {status}, Symptoms: {', '.join(self.symptoms)}, Prescribed Doctor: {self.prescribed_doctor}"
        pass
    def record_symptoms(self, new_symptoms):
        self.symptoms.extend(new_symptoms)
        print(f"Symptoms for patient '{self.name}' updated: {', '.join(self.symptoms)}")
    def get_medical_history(self):
        return f"Medical History for {self.name}: {self.medical_history}"
class Doctor:
    def __init__ (self, name, speciality, years_of_experience, current_patients = [], status = "Available", work_shedule = "9am-5pm"):
        self.name = name
        self.speciality = speciality
        self.years_of_experience = years_of_experience
        self.current_patients = current_patients
        self.status = status
        self.work_shedule = work_shedule
    def 