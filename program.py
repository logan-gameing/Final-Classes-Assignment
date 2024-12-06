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

    def search_doctor_by_id(self):
        docId = input("Enter the doctor Id: ")
        for i in self.doctors:
            if i.id == docId:
                self.display_doctor_info(i)
                break

    def search_doctor_by_name(self):
        docName = input("Enter the doctor name: ")
        for i in self.doctors:
            if i.name == docName:
                self.display_doctor_info(i)
                break

    def display_doctor_info(self, doc):
        print(f"{"Id":<6}{"Name":<20}{"Speciality":<16}{"Timing":<12}{"Qualification":<20}Room Number\n")
        print(f"{doc.id:<6}{doc.name:<20}{doc.specialization:<16}{doc.working_time:<12}{doc.qualifications:<20}{doc.room_number}\n")

    def edit_doctor_info(self):
        toEdit = input("Please enter the id of the doctor that you want to edit their information:")
        for i in self.doctors:
            if toEdit in i.id:
                newDoc = Doctor()
                newDoc.id = i.id
                newDoc.name = input("Enter new Name:")
                newDoc.specialization = input("Enter new Specialist in:")
                newDoc.working_time = input("Enter new Timing:")
                newDoc.qualifications = input("Enter new Qualification:")
                newDoc.room_number = input("Enter new Room Number:")
                i = newDoc
                #EDIT DOCKTOR

        print("Cannot find the doctor...")


    def display_doctors_list(self):
        print(f"{"Id":<6}{"Name":<20}{"Speciality":<16}{"Timing":<12}{"Qualification":<20}Room Number\n")
        for i in self.doctors[1:]:
            print(f"{i.id:<6}{i.name:<20}{i.specialization:<16}{i.working_time:<12}{i.qualifications:<20}{i.room_number}\n")

    def Write_list_of_doctors_to_file(self):
        print("TEMP")

    def add_dr_to_file(self):
        print("TEMP")

manager = DoctorManager()
manager.search_doctor_by_id()
