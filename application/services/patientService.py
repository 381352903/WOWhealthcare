from OLTP import databaseService


def register_patient(patient):
    databaseService.insert_record('patient', patient)