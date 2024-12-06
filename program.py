#Logan


class Doctor():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.specialization = ''
        self.working_time = ''
        self.qualifications = ''
        self.room_number = ''

    def get_doctor_id(self):
        return self.id
    def get_doctor_name(self):
        return self.name
    def get_doctor_specialize(self):
        return self.specialization
    def get_doctor_work_time(self):
        return self.working_time
    def get_doctor_qualify(self):
        return self.qualifications
    def get_doctor_room_number(self):
        return self.room_number

    def set_doctor_id(self, new_id):
        self.id = new_id
    def set_doctor_name(self, new_name):
        self.name = new_name
    def set_doctor_specialize(self, new_specialization):
        self.specialization = new_specialization
    def set_doctor_work_time(self, new_work_time):
        self.working_time = new_work_time
    def set_doctor_qualify(self, new_qualifications):
        self.qualifications = new_qualifications
    def set_doctor_room_number(self, new_room_number):
        self.room_number = new_room_number
    def __str__(self):
        return f"{self.id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualifications}_{self.room_number}"


class DoctorManager():
    def __init__(self):
        self.doctors = self.read_doctors_file()

        for a in self.doctors:
            print(a)

        #READ DOCDOR
        

    def format_dr_info(self):
        print("EMPY")

    def enter_dr_info(self):
        newDoc = Doctor()
        newDoc.id = input("Enter Doctor ID")
        newDoc.name = input("Enter Doctor Name")
        newDoc.specialization = input("Enter Doctors Specialization")
        newDoc.working_time = input("Enter Doctors Working Times")
        newDoc.qualifications = input("Enter Doctors Qualifications")
        newDoc.room_number = input("Enter Doctors Room Number")
        return newDoc

    def read_doctors_file(self):
        array = []
        with open('doctors.txt','r') as f:
            for line in f:
                #print(line.strip().split("_"))
                temp = line.strip().split("_")
                newDoc = Doctor()
                newDoc.id = temp[0]
                newDoc.name = temp[1]
                newDoc.specialization = temp[2]
                newDoc.working_time = temp[3]
                newDoc.qualifications = temp[4]
                newDoc.room_number = temp[5]
                array.append(newDoc)
        return array

print("P1")
a = DoctorManager()
