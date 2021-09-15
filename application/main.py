import datetime

from services import patientService
from services import doctorService
from OLTP import databaseService

if __name__ == '__main__':
    date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    patient_model = {'Name': 'test1', 'Address': '235 grand ST.', 'PhoneNumber': '3322349999',
               'RelationshipWithEmergencyContact': 'Parent',
               'EmergencyContact': 'Zhang', 'IsInPatient': True, 'FollowUpDate': date_time, 'BedNumber': 3,
               'Floor': 2,
               'DischargeDate': date_time, 'TableLastDate': date_time}

    command = ''
    while command != 'exit':
        command = input('What do you want to do:')
        if command == 'register a patient model':
            patientService.register_patient(patient_model)
        elif command == 'register a patient':
            patient = {}
        elif command == 'show patients':
            databaseService.show_data('patient')
        elif command == 'show patients columns':
            databaseService.show_columns('patient')



