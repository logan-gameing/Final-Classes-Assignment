#Logan

class DoctorManager():
    def __init__(self):
        self.doctors = []

        print("P2")

        #READ DOCDOR
        self.read_doctors_file()

    def format_dr_info(self):
        print("EMPY")

    def enter_dr_info(self):
        print("EMPY")

    def read_doctors_file(self):

        with open('doctors.txt','r') as f:
            for line in f:
                print(line.replace("_", " "))
                

print("P1")
a = DoctorManager()
