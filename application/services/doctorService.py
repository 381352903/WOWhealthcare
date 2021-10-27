from OLTP import databaseService
from application import main
from application.services.paymentService import generate_invoice

def register_doctor():
    databaseService.show_columns('doctor')
    doctor_model = main.read_dict()
    databaseService.insert_record('doctor', doctor_model)
    databaseService.show_data('doctor')

def initiate_treatment(account_id, registration_id):
    databaseService.show_columns('treatment')
    print('TreatmentType, DiseaseId are not null')
    treatment_model = main.read_dict()
    treatment_model['DoctorId'] = account_id
    treatment_model['TreatmentDate'] = databaseService.get_cur_time()
    treatment_model['RegistrationId'] = registration_id
    treatment_model['DoctorId'] = account_id
    treatment_id = databaseService.insert_record('treatment', treatment_model)
    print(databaseService.search_data('treatment', 'DoctorId=' + str(account_id)))
    # update table: patient_treatment
    end_registration(registration_id, treatment_id)

def update_treatment(treatment_id):
    databaseService.show_columns('treatment')
    treatment_model = main.read_dict()
    filter = 'TreatmentId=' + str(treatment_id)
    databaseService.update_record('treatment', filter, treatment_model)
    print(databaseService.search_data('treatment', 'TreatmentId=' + str(treatment_id)))
    
def end_registration(registration_id, treatment_id):
    d = {'HasProcessed': True, 'TreatmentId': treatment_id}
    filter = 'RegistrationId=' + registration_id
    databaseService.update_record('registration', filter, d)

def finish_treatment(treatment_id, status: str):
    d = {'ResultStatus': status}
    filter = 'TreatmentId=' + str(treatment_id)
    databaseService.update_record('treatment', filter, d)
    tmp_data = databaseService.search_data('treatment', 'treatment=' + str(treatment_id))
    registration_id = tmp_data['RegistrationId']
    patient_id = tmp_data['PatientId']
    print('Input the costs for lab_cost, drug_cost, surgery_cost, bed_cost, bill_to_insurance')
    cost_dict = main.read_dict()
    generate_invoice(registration_id, patient_id, cost_dict['lab_cost'], cost_dict['drug_cost'], cost_dict['surgery_cost'], cost_dict['bed_cost'], cost_dict['bill_to_insurance'])
    return None

def diagnose_disease():
    databaseService.show_columns('disease')
    disease_model = main.read_dict()
    databaseService.insert_record('disease', disease_model)


def doctor_commands(account_id):
    command = input(
        '1. Check my treatment                      \n'
            # update treatment status
                # if completed or terminated, call generate_invoice
        '2. Check available registration            \n'
            # diagnose a disease (insert a disease into disease table for this patient)
            # give treament:
            # (Add a new treatment into treatment table
            # update registration HasProcessed boolean )
                # update treatment status  
                    # if completed or terminated, call generate_invoice
        '3. Registration for a new disease                \n'
    )
    if command == '1':
        # Check all treatment under this doctor
        print(databaseService.search_data('treatment', 'DoctorId=' + str(account_id)))
        treatment_id = input('Do you want to update the treatment?(Input the '
                                'treatment id or no)\n')
        if treatment_id != 'no':
            update_treatment(treatment_id)
            # update treatment status 
    elif command == '2':
        # Check all registration which have not been processed
        print(databaseService.search_data('registration', 'HasProcessed IS NOT True'))
        registration_id = input('Do you want to work on a registration?(Input the '
                                'registration id or no)\n')
        if registration_id != 'no':
            # diagnose a disease 
            initiate_treatment(account_id, registration_id)
            # update treatment status
    elif command == '3':
        diagnose_disease()
