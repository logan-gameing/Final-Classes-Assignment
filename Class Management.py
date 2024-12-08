class Management:
  def __init__(self):
    self.doctor_manager = DoctorManager()
    self.patient_manager = PatientManager()

  def display_menu(self):
    while True:
      options= input('\nWelcome to Alberta Hospital (AH) Manager Systems/nSelect from the following options, or select 3 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n>>>')
      if options  == '1':
        self.doctors_menu()
      elif options == '2':
        self.patients_menu()
      elif options == '3':
        print('Thanks for using the program. Bye!')
        break
      else:
        print('Invalid choice. Please try again.')

  def doctors_menu(self):
    while True:
      options= input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the main menu\n>>>')
      if options == '1':
        self.doctor_manager.display_doctors_list()
      elif options == '2':
        self.doctor_manager.search_doctor_by_id()
      elif options == '3':
        self.doctor_manager.search_doctor_by_name()
      elif options == '4':
        self.doctor_manager.add_dr_to_file()
      elif options == '5':
        self.doctor_manager.edit_doctor_info()
      elif options == '6':
        break
      else:
        print('Invalid choice. Please try again.')

  def patients_menu(self):
    while True:
      options= input('\nPatients Menu:\n1 - Display Patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the main menu\n>>>')
      if options == '1':
        self.patient_manager.display_patients_list()
      elif options == '2':
        self.patient_manager.search_patient_by_id()
      elif options == '3':
        self.patient_manager.add_patient_to_file()
      elif options == '4':
        pid= int(input('Enter patient id:'))
        self.patient_manager.edit_patient_info_by_id(pid)
      elif options == '5':
        break
      else:
        print('Invalid choice. Please try again.')

if __name__ == '__main__':
  management = Management()
  management.display_menu()
