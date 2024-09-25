# Hospital Management System

class Patient:
    def __init__(self, id, name, age, gender, ailment):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.ailment = ailment

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Ailment: {self.ailment}"


class Doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Specialty: {self.specialty}"


class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, id, name, age, gender, ailment):
        new_patient = Patient(id, name, age, gender, ailment)
        self.patients.append(new_patient)
        print(f"Patient {name} added successfully!")

    def view_patient(self, id):
        for patient in self.patients:
            if patient.id == id:
                print(patient)
                return
        print("Patient not found!")

    def add_doctor(self, id, name, specialty):
        new_doctor = Doctor(id, name, specialty)
        self.doctors.append(new_doctor)
        print(f"Doctor {name} added successfully!")

    def view_doctor(self, id):
        for doctor in self.doctors:
            if doctor.id == id:
                print(doctor)
                return
        print("Doctor not found!")

    def add_appointment(self, patient_id, doctor_id):
        patient = next((p for p in self.patients if p.id == patient_id), None)
        doctor = next((d for d in self.doctors if d.id == doctor_id), None)

        if patient and doctor:
            appointment = {"patient": patient, "doctor": doctor}
            self.appointments.append(appointment)
            print(f"Appointment scheduled: {patient.name} with Dr. {doctor.name}")
        else:
            print("Invalid patient or doctor ID!")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
            return

        for appointment in self.appointments:
            print(f"Patient: {appointment['patient'].name}, Doctor: {appointment['doctor'].name}")

def main():
    hms = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Add Doctor")
        print("4. View Doctor")
        print("5. Schedule Appointment")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            ailment = input("Enter patient ailment: ")
            hms.add_patient(id, name, age, gender, ailment)

        elif choice == '2':
            id = input("Enter patient ID: ")
            hms.view_patient(id)

        elif choice == '3':
            id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialty = input("Enter doctor specialty: ")
            hms.add_doctor(id, name, specialty)

        elif choice == '4':
            id = input("Enter doctor ID: ")
            hms.view_doctor(id)

        elif choice == '5':
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            hms.add_appointment(patient_id, doctor_id)

        elif choice == '6':
            hms.view_appointments()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1445