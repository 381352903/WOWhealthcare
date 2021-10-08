import random

from OLTP import databaseService
from application import main
from application.services import paymentService


_CONSTANT_NUMBER = 1234567


def register_patient():
    databaseService.show_columns('patient')
    patient_model = main.read_dict()
    databaseService.insert_record('patient', patient_model)
    databaseService.show_data('patient')

def registration_for_treatment(account_id):
    databaseService.show_columns('registration')
    registration_model = {'PatientId': account_id, 'RegistrationDate': str(databaseService.get_cur_time()),
                          'RegistrationNumber': int(random.random() * _CONSTANT_NUMBER)}
    databaseService.insert_record('registration', registration_model)
    print('Registered successfully, remember your registration id! You just need to wait for doctors '
          'treatments.\n')
    print(databaseService.search_data('registration', 'PatientId=' + str(account_id)))


'''
    1. registration, waiting for the diagnose and treatment from doctor
    2. if the patient has invoices to pay, he can make payments for that
'''


def patient_commands(account_id):
    command = input(
        '1. Make a registration for your treatment      \n'
        '2. Check my registrations balances             \n'
        '3. Check my payments                           \n'
    )
    if command == '1':
        registration_for_treatment(account_id)
    elif command == '2':
        print(paymentService.get_balance_for_all_registration(account_id))
        registration_id = input('Do you want to make a payment for the registration?(Input the '
                                'registration id or no)\n')
        if registration_id != 'no' and registration_id != 'No':
            amount = input(
                'How much money do you want to pay for the registration with id:' + registration_id + '?(input the amount:\n)')
            pay_type = input('How would you like to make the payment?(Credit Card, Debit Card, EFT, Check)\n')
            payment_model = {'PaymentDate': str(databaseService.get_cur_time()), 'Amount': str(amount), 'Type': pay_type,
                             'RegistrationId': registration_id, 'PatientId': account_id}
            databaseService.insert_record('payment', payment_model)
    elif command == '3':
        print(databaseService.search_data('payment', 'PatientId=' + str(account_id)))