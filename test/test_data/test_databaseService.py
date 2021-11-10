# Hospital Table
HOSPITAL_MODEL1 = {
    'HospitalId': 10001, 
    'Name': 'NYU LAGONE HEALTH', 'Address': '550 1st Avenue', 'Specialty': 'Surgery', 'EmergencyHotlineNumbers': '7186307185',
    'GeneralInquiryPhoneNumbers': '6469297875', 'RegistrationNumber': '10001', 'DepartmentNames': 'SURGERY',
    'DepartmentLocation': 'Floor 12', 'TableLastDate': '2021-11-09 14:46:05',
}
HOSPITAL_MODEL2 = {
    'HospitalId': 10002, 
    'Name': 'Harbor Healthcare System', 'Address': '423 E 23rd St', 'Specialty': 'Medical Clinic', 'EmergencyHotlineNumbers': '2126867500',
    'GeneralInquiryPhoneNumbers': '2129513240', 'RegistrationNumber': '10002', 'DepartmentNames': 'Medical Clinic',
    'DepartmentLocation': 'Floor 3', 'TableLastDate': '2021-11-09 14:46:05',
}
HOSPITAL_MODEL3 = {
    'HospitalId': 10003, 
    'Name': 'NYC Health + Hospitals / Bellevue', 'Address': '462 1st Avenue', 'Specialty': 'Neurology Care', 'EmergencyHotlineNumbers': '8446924692',
    'GeneralInquiryPhoneNumbers': '2125624141', 'RegistrationNumber': '10003', 'DepartmentNames': 'Neurology Care',
    'DepartmentLocation': 'Floor 5', 'TableLastDate': '2021-11-09 14:46:05',
}

# Doctor Table 
DOCTOR_MODEL1 = {
    'DoctorId': 101, 'Name': 'Dr.Zhang', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(853) 467-3964', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 400000, 'ContractDate': None,
    'ContractNumber': None, 'WeeklyContractRate': None, 'MinWeeklyHours': None, 'OvertimeRatePerHour': None, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL2 = {
    'DoctorId': 102, 'Name': 'Stephanie', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(441) 866-4376', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 350000, 'ContractDate': None,
    'ContractNumber': None, 'WeeklyContractRate': None, 'MinWeeklyHours': None, 'OvertimeRatePerHour': None, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL3 = {
    'DoctorId': 103, 'Name': 'Kelly', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(390) 383-2329', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 450000, 'ContractDate': None,
    'ContractNumber': None, 'WeeklyContractRate': None, 'MinWeeklyHours': None, 'OvertimeRatePerHour': None, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL4 = {
    'DoctorId': 104, 'Name': 'George', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(505) 616-4179', 'Specialty': 'Neurology Care',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 300000, 'ContractDate': None,
    'ContractNumber': None, 'WeeklyContractRate': None, 'MinWeeklyHours': None, 'OvertimeRatePerHour': None, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL5 = {
    'DoctorId': 105, 'Name': 'Marion', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(756) 496-3786', 'Specialty': 'Neurology Care',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 280000, 'ContractDate': None,
    'ContractNumber': None, 'WeeklyContractRate': None, 'MinWeeklyHours': None, 'OvertimeRatePerHour': None, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL6 = {
    'DoctorId': 106, 'Name': 'Dr.Zhang', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(432) 861-4072', 'Specialty': 'Neurology Care',
    'HireDate': None, 'YearlyCompensation': None, 'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 1, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL7 = {
    'DoctorId': 107, 'Name': 'Frank', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(963) 411-5643', 'Specialty': 'Surgery',
    'HireDate': None, 'YearlyCompensation': None, 'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 2, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL8 = {
    'DoctorId': 108, 'Name': 'Henry', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(344) 497-2106', 'Specialty': 'Surgery',
    'HireDate': None, 'YearlyCompensation': None, 'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 3, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL9 = {
    'DoctorId': 109, 'Name': 'Maria', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(859) 840-2596', 'Specialty': 'Surgery',
    'HireDate': None, 'YearlyCompensation': None, 'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 4, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL10 = {
    'DoctorId': 110, 'Name': 'Kyle', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(960) 240-5857', 'Specialty': 'Surgery',
    'HireDate': None, 'YearlyCompensation': None, 'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 5, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}

# Disease Table
DISEASE_MODEL1 = {
    'DiseaseId': 201, 
    'ICD': 'E66.9', 'Discription': 'Obesity, unspecified', 
    'Type': 'Physiologic', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL2 = {
    'DiseaseId': 202, 
    'ICD': 'S52', 'Description': 'Fracture of forearm', 
    'Type': 'Injuries', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL3 = {
    'DiseaseId': 203, 
    'ICD': 'I50.810', 'Description': 'Right heart failure, unspecified', 
    'Type': 'Deficiency', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL4 = {
    'DiseaseId': 204, 
    'ICD': 'K02', 'Description': 'Dental caries', 
    'Type': 'Physiologic', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL5 = {
    'DiseaseId': 205, 
    'ICD': 'K14', 'Description': 'Diseases of tongue', 
    'Type': 'Viral', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL6 = {
    'DiseaseId': 206, 
    'ICD': 'R50', 'Description': 'Fever of other and unknown origin', 
    'Type': 'Seasonal', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL7 = {
    'DiseaseId': 207, 
    'ICD': 'R51', 'Description': 'HEADACHE', 
    'Type': 'Physiologic', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL8 = {
    'DiseaseId': 208, 
    'ICD': 'S01', 'Description': 'Open wound of head', 
    'Type': 'Injuries', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL9 = {
    'DiseaseId': 209, 
    'ICD': 'S11', 'Description': 'Open wound of neck', 
    'Type': 'Injuries', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL10 = {
    'DiseaseId': 210, 
    'ICD': 'S26', 'Description': 'Injury of heart', 
    'Type': 'Injuries', 'TableLastDate': '2021-11-09 14:46:05',
}

# Patient Table
PATIENT_MODEL1 = {'PatientID': 1, 'Name': 'Emma', 'Address': '235 grand ST.', 'PhoneNumber': '3322349999',
           'RelationshipWithEmergencyContact': 'Parent',
           'EmergencyContact': 'Zhang', 'IsInPatient': True, 'FollowUpDate': '2021-09-17 15:01:11', 'BedNumber': 3,
           'Floor': 2,
           'DischargeDate': '2021-09-17 15:01:11', 'TableLastDate': '2021-09-17 15:01:11'}

PATIENT_MODEL2 = {'PatientID': 2, 'Name': 'John', 'Address': '475 Washington Street', 'PhoneNumber': '2128808800',
           'RelationshipWithEmergencyContact': 'Partner',
           'EmergencyContact': 'Wang', 'IsInPatient': True, 'FollowUpDate': '2021-10-05 09:28:55', 'BedNumber': 5,
           'Floor': 6,
           'DischargeDate': '2021-10-05 09:28:55', 'TableLastDate': '2021-10-05 09:28:55'}

PATIENT_MODEL3 = {'PatientID': 3, 'Name': 'Joshua', 'Address': '235 grand ST.', 'PhoneNumber': '7704981172',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Feng', 'IsInPatient': True, 'FollowUpDate': '2021-07-25 12:09:42', 'BedNumber': 10,
           'Floor': 4,
           'DischargeDate': '2021-07-25 12:09:42', 'TableLastDate': '2021-07-25 12:09:42'}

PATIENT_MODEL4 = {'PatientID': 4, 'Name': 'Leslie', 'Address': '615 Pavonia Ave', 'PhoneNumber': '3322349999',
           'RelationshipWithEmergencyContact': 'Mother',
           'EmergencyContact': 'Maria', 'IsInPatient': True, 'FollowUpDate': '2021-09-09 14:22:32', 'BedNumber': 112,
           'Floor': 11,
           'DischargeDate': '2021-09-09 14:22:32', 'TableLastDate': '2021-09-09 14:22:32'}

PATIENT_MODEL5 = {'PatientID': 5, 'Name': 'Christine', 'Address': '90 Columbus Drive', 'PhoneNumber': '1654891374',
           'RelationshipWithEmergencyContact': 'Father',
           'EmergencyContact': 'John', 'IsInPatient': False, 'FollowUpDate': '2021-02-15 09:36:32', 'BedNumber': None,
           'Floor': None,
           'DischargeDate': None, 'TableLastDate': '2021-02-15 09:36:32'}

PATIENT_MODEL6 = {'PatientID': 6, 'Name': 'Leslie', 'Address': '70 Columbus Drive', 'PhoneNumber': '6549997164',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Kai', 'IsInPatient': True, 'FollowUpDate': '2021-10-21 11:05:46', 'BedNumber': 25,
           'Floor': 5,
           'DischargeDate': '2021-10-21 11:05:46', 'TableLastDate': '2021-10-21 11:05:46'}

PATIENT_MODEL7 = {'PatientID': 7, 'Name': 'Mila', 'Address': '475 Washington Street', 'PhoneNumber': '8412546184',
           'RelationshipWithEmergencyContact': 'Husband',
           'EmergencyContact': 'Jerry', 'IsInPatient': False, 'FollowUpDate': '2021-10-06 16:28:55', 'BedNumber': None,
           'Floor': None,
           'DischargeDate': None, 'TableLastDate': '2021-10-06 16:28:55'}

PATIENT_MODEL8 = {'PatientID': 8, 'Name': 'Zion', 'Address': '475 Washington Street', 'PhoneNumber': '3467816455',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Bob', 'IsInPatient': False, 'FollowUpDate': '2021-10-08 11:28:12', 'BedNumber': None,
           'Floor': None,
           'DischargeDate': None, 'TableLastDate': '2021-10-08 11:28:12'}

# Treatment Table
TREATMENT_MODEL = {'TreatmentId': 1, 'DoctorId': 1, 'TreatmentDate': '', 'TreatmentType': '',
           'ResultStatus': '', 'Description': None, 'LabName': None, 'TestType': None,
           'TestDate': None, 'TestResult': None, 'DrugName': None, 'DrugDose': None,
           'SurgeryName': None, 'SurgeryDescription': None, 'SurgeryDate': None, 'SurgeryResult': None,
           'TableLastDate': None, 'RegistrationId': 1,
}

# Payment Table
PATIENT_MODEL8 = {'PatientID': 8, 'Name': 'Zion', 'Address': '475 Washington Street', 'PhoneNumber': '3467816455',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Bob', 'IsInPatient': False, 'FollowUpDate': '2021-10-08 11:28:12', 'BedNumber': None,
           'Floor': None,
           'DischargeDate': None, 'TableLastDate': '2021-10-08 11:28:12'}

# NEED 3
REGISTRATION_MODEL = {

}
# NEED 2
INVOICE_MODEL = {

}
# NEED 3
PAYMENT_MODEL = {

}
