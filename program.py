#Logan
import os

class DoctorManager():
    def __init__(self):
        doctors = []

        #READ DOCDOR

    def format_dr_info():
        print("EMPY")

    def enter_dr_info():
        print("EMPY")

    def read_doctors_file():
        print("EMPY")

        f_obj = open('/doctors.txt', 'r')

        line = f_obj.readline()
        while line != '':
            line = line.rstrip()
            print(line)
            line = f_obj.readline()
            f_obj.close()

a = DoctorManager()
a.read_doctors_file