from OLTP import databaseService

_CONSTANT_NUMBER = 1234567

def generate_invoice(registration_id, patient_id, lab_cost = 0, drug_cost = 0, surgery_cost = 0, bed_cost = 0, bill_to_insurance = 0):
    total_cost = lab_cost + drug_cost + surgery_cost + bed_cost
    copy_total_cost = total_cost
    if bill_to_insurance >= total_cost:
        total_cost = 0
    else:
        total_cost -= bill_to_insurance
    model = {
        'InvoiceNumber': int(random.random() * _CONSTANT_NUMBER), 'InvoiceDate': databaseService.get_cur_time(),
         'LabCost': lab_cost, 'DrugCost': drug_cost, 'SurgeryCost': surgery_cost, 'BedUsageCost': bed_cost, 'TotalCost': copy_total_cost,
         'BillToInsurance': bill_to_insurance, 'CostToPatient': total_cost, 'RegistrationId': registration_id,
         'PatientId': patient_id
             }
    databaseService.insert_record('invoice', model)

# leave it alone
def make_payment():
    return None


def get_balance_for_all_registration(account_id):
    registrations = databaseService.search_data('Registration', 'PatientId=' + str(account_id))
    d = {}
    for index, row in registrations.iterrows():
        reg_idx = str(row['RegistrationId'])
        invoices = databaseService.search_data('invoice', 'RegistrationId=' + reg_idx)
        payments = databaseService.search_data('payment', 'RegistrationId=' + reg_idx)
        cost = 0
        pay = 0
        for index1, row1 in invoices.iterrows():
            cost += int(row1['TotalCost'])
        for index2, row2 in payments.iterrows():
            pay += int(row2['Amount'])
        d[reg_idx] = 'need to pay: $ ' + str(cost - pay)
    return d





