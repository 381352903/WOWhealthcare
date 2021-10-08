from OLTP import databaseService


def generate_invoice():
    return None

# leave it alone
def make_payment():
    return None


def get_balance_for_all_registration(account_id):
    registrations = databaseService.search_data('Registration', 'PatientId=' + str(account_id))
    d = {}
    for index, row in registrations.iterrows():
        reg_idx = str(row['Id'])
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





