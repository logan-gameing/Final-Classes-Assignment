#Logan

class DoctorManager():
    def __init__(self):
        self.doctors = self.read_doctors_file()

        print(self.doctors)

        #READ DOCDOR
        

    def format_dr_info(self):
        print("EMPY")

    def enter_dr_info(self):
        print("EMPY")

    def read_doctors_file(self):
        array = []
        with open('doctors.txt','r') as f:
            for line in f:
                print(line.replace("_", " "))
                array.append(line.replace("_", " "))

        return array

print("P1")
a = DoctorManager()
