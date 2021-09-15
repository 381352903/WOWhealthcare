from OLTP import databaseService


def register_doctor(doctor):
    databaseService.insert_record('doctor', doctor)