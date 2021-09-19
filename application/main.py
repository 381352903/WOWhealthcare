import datetime

from services import patientService
from services import doctorService
from OLTP import databaseService
from test.test_data import test_databaseService


_GUEST = '0'
_PATIENT = '1'
_DOCTOR = '2'
_ADMIN = '3'


'''
    @Description:
        Each time we want to insert record or update the records in the databases,
        we will input a dict manually, the keys of the dict are the columns of the record,
        the values of the dict is values of the record in the database
    @Return:
        return the dict
'''


def read_dict():
    keys = None
    values = None
    while keys is None or values is None or len(keys) != len(values):
        keys = input("Please input the keys(split by ',')")
        keys = keys.split(',')
        values = input("Please input the values(split by ',')")
        values = values.split(',')
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d


if __name__ == '__main__':
    command = ''
    identity = _GUEST
    account_id = -1
    while command != 'exit':
        while identity != _PATIENT and identity != _DOCTOR and identity != _ADMIN:
            identity = input('Who are you?(Patient: 1 or Doctor: 2 or Admin: 3) \n')
        print('What do you want to do: \n')
        if identity == _PATIENT and account_id == -1:
            command = input(
                            '1. You are a new patient(Register an account)      \n'
                            '2. You have an account(Login)                      \n'
                            '3. Show all patients                               \n'
                            )
            if command == '1':
                patientService.register_patient()
            elif command == '2':
                account_id = int(input('Input your id: \n'))
                patientService.patient_commands(account_id)
            elif command == '3':
                databaseService.show_data('patient')
        elif identity == _PATIENT:
            patientService.patient_commands(account_id)
        elif identity == _DOCTOR:
            '''
                ???????????????????????????????????????????
                @@@@This part can be implemented by you@@@@
                ???????????????????????????????????????????
            '''
            command = input(
                            '1. You are a new doctor(Register an account)   \n'
                            '2. You have an doctor(Login)                   \n'
                            )
            if command == '1':
                databaseService.show_columns('doctor')
                patient_model = read_dict()
                databaseService.insert_record('doctor', patient_model)
            elif command == '2':
                '''
                    1. diagnose a patient's disease for each registration
                        i. only insert the newly found disease into the 'disease' database
                    2. give a treatment for each registration(one-to-one)
                        i. insert a new treatment record for each registration
                        ii. insert doctor_disease table
                        iii. insert patient_treatment table
                        iv. insert the patient_doctor table
                    3. complete a treatment by updating the treatment status
                        i. for each treatment, we can update its status
                        ii. if the status is update as terminated or completed, call generate_invoice for the treatment
                    4. the program is fairly flexible, you can design as you want as long as reasonable
                '''
        elif identity == _ADMIN:
            command = input(
                            '1. Register a new hospital     \n'
                            '2. Change your identity        \n'
                            '3. Insert a patient model      \n'
                            '4. Show patient database       \n'
                            )
            if command == '1':
                databaseService.show_columns('hospital')
                hospital_model = read_dict()
                databaseService.insert_record('hospital', hospital_model)
            elif command == '2':
                identity = '0'
            elif command == '3':
                databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL)
            elif command == '4':
                databaseService.show_data('patient')
