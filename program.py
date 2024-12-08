class DoctorManager():
    def __init__(self):
        self.doctors = self.read_doctors_file()


    def format_dr_info(self, doc):
        return str(doc)

    def enter_dr_info(self):
        newDoc = Doctor()
        newDoc.id = input("Enter Doctor's ID: ")
        newDoc.name = input("Enter Doctor's Name: ")
        newDoc.specialization = input("Enter Doctor's Specialization: ")
        newDoc.working_time = input("Enter Doctor's Working Times (e.g., 7am-10pm): ")
        newDoc.qualifications = input("Enter Doctor's Qualification: ")
        newDoc.room_number = input("Enter Doctor's Room Number: ")
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
        else:
          print('Can\'t find the doctor with the same ID on the system')


    def search_doctor_by_name(self):
        docName = input("Enter the doctor name: ")
        for i in self.doctors:
          if i.name == docName:
            self.display_doctor_info(i)
            break
        else:
          print('Can\'t find the doctor with the same name on the system')


    def display_doctor_info(self, doc):
        print(f"{'Id':<6}{'Name':<20}{'Speciality':<16}{'Timing':<12}{'Qualification':<20}Room Number\n")
        print(f"{doc.id:<6}{doc.name:<20}{doc.specialization:<16}{doc.working_time:<12}{doc.qualifications:<20}{doc.room_number}\n")

    def edit_doctor_info(self):
        toEdit = input("Please enter the id of the doctor that you want to edit their information: ")
        for i in self.doctors:
            if toEdit in i.id:
                newDoc = Doctor()
                newDoc.id = i.id
                newDoc.name = input("Enter new Name: ")
                newDoc.specialization = input("Enter new Specialist in: ")
                newDoc.working_time = input("Enter new Timing: ")
                newDoc.qualifications = input("Enter new Qualification: ")
                newDoc.room_number = input("Enter new Room Number: ")
                i = newDoc
                print(f"Doctor whose ID is {newDoc.id} has been edited.")
                break
                #EDIT DOCKTOR

    def display_doctors_list(self):
        print(f"{'Id':<6}{'Name':<20}{'Speciality':<16}{'Timing':<12}{'Qualification':<20}Room Number\n")
        for i in self.doctors[1:]:
            print(f"{i.id:<6}{i.name:<20}{i.specialization:<16}{i.working_time:<12}{i.qualifications:<20}{i.room_number}\n")

    def Write_list_of_doctors_to_file(self):
        with open('doctors.txt','w') as f:
            for i in self.doctors:
                f.writelines(str(f"{i}\n"))

    def add_dr_to_file(self):
        #create new doctor and add to list
        newDoc = self.enter_dr_info()
        self.doctors.append(newDoc)
        print(f"Doctor whose ID is {newDoc.id} has been added.")
        self.Write_list_of_doctors_to_file()
