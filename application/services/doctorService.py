from OLTP import databaseService


def register_doctor(doctor):
    databaseService.insert_record('doctor', doctor)


def end_registration(registration_id):
    d = {'HasProcessed': True}
    databaseService.update_record('registration', int(registration_id), d)
