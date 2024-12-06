#Logan
import os

class DoctorManager():
    def __init__(self):
        self.doctors = []

        print("P2")

        #READ DOCDOR

    def format_dr_info():
        print("EMPY")

    def enter_dr_info():
        print("EMPY")

    def read_doctors_file():
        print("P3")

        f_obj = open('/doctors.txt', 'r')

        line = f_obj.readline()
        while line != '':
            line = line.rstrip()
            print(line)
            line = f_obj.readline()
            f_obj.close()

print("P1")
a = DoctorManager()
a.read_doctors_file