from OLTP import databaseService
from test.test_data import test_databaseService

if __name__ == '__main__':
    databaseService.insert_record('hospital', test_databaseService.HOSPITAL_MODEL1)
    databaseService.insert_record('hospital', test_databaseService.HOSPITAL_MODEL2)
    databaseService.insert_record('hospital', test_databaseService.HOSPITAL_MODEL3)

    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL1)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL2)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL3)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL4)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL5)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL6)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL7)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL8)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL9)
    databaseService.insert_record('doctor', test_databaseService.DOCTOR_MODEL10)

    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL1)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL2)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL3)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL4)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL5)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL6)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL7)
    databaseService.insert_record('patient', test_databaseService.PATIENT_MODEL8)

    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL1)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL2)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL3)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL4)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL5)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL6)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL7)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL8)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL9)
    databaseService.insert_record('disease', test_databaseService.DISEASE_MODEL10)

    #databaseService.insert_record('disease', test_databaseService.PAYMENT_MODEL)
