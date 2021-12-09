# Hospital Table
HOSPITAL_MODEL1 = {
    'HospitalId': 10001, 
    'Name': 'NYU LAGONE HEALTH', 'Address': '550 1st Avenue', 'Specialty': 'Surgery', 'EmergencyHotlineNumbers': '7186307185',
    'GeneralInquiryPhoneNumbers': '6469297875', 'RegistrationNumber': '10001', 
    'TableLastDate': '2021-11-09 14:46:05',
}
HOSPITAL_MODEL2 = {
    'HospitalId': 10002, 
    'Name': 'Harbor Healthcare System', 'Address': '423 E 23rd St', 'Specialty': 'Medical Clinic', 'EmergencyHotlineNumbers': '2126867500',
    'GeneralInquiryPhoneNumbers': '2129513240', 'RegistrationNumber': '10002', 
    'TableLastDate': '2021-11-09 14:46:05',
}
HOSPITAL_MODEL3 = {
    'HospitalId': 10003, 
    'Name': 'NYC Health + Hospitals / Bellevue', 'Address': '462 1st Avenue', 'Specialty': 'Dental', 'EmergencyHotlineNumbers': '8446924692',
    'GeneralInquiryPhoneNumbers': '2125624141', 'RegistrationNumber': '10003', 'DepartmentNames': 'Dental',
    'DepartmentLocation': 'Floor 5', 'TableLastDate': '2021-11-09 14:46:05',
}

# Doctor Table 
DOCTOR_MODEL1 = {
    'DoctorId': 101, 'Name': 'Dr.Zhang', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(853) 467-3964', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 400000, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL2 = {
    'DoctorId': 102, 'Name': 'Stephanie', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(441) 866-4376', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 350000, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL3 = {
    'DoctorId': 103, 'Name': 'Kelly', 'OfficePhoneNumber': '2129513240', 'PersonalPhoneNumber': '(390) 383-2329', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 300000, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL4 = {
    'DoctorId': 104, 'Name': 'George', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(505) 616-4179', 'Specialty': 'Neurology Care',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 400000, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL5 = {
    'DoctorId': 105, 'Name': 'Marion', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(756) 496-3786', 'Specialty': 'Neurology Care',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 200000, 'IsFullTime': True,
    'HospitalId': 10001,
}
DOCTOR_MODEL6 = {
    'DoctorId': 106, 'Name': 'Dr.Zhang', 'OfficePhoneNumber': '2125624141', 'PersonalPhoneNumber': '(432) 861-4072', 'Specialty': 'Oncology',
    'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 1, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL7 = {
    'DoctorId': 107, 'Name': 'Frank', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(963) 411-5643', 'Specialty': 'Surgery',
    'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 2, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10001,
}
DOCTOR_MODEL8 = {
    'DoctorId': 108, 'Name': 'Henry', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(344) 497-2106', 'Specialty': 'Surgery',
    'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 3, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10001,
}
DOCTOR_MODEL9 = {
    'DoctorId': 109, 'Name': 'Maria', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(859) 840-2596', 'Specialty': 'Surgery',
    'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 4, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10002,
}
DOCTOR_MODEL10 = {
    'DoctorId': 110, 'Name': 'Kyle', 'OfficePhoneNumber': '6469297875', 'PersonalPhoneNumber': '(960) 240-5857', 'Specialty': 'Dental',
    'ContractDate': '2020-09-01 08:00:00',
    'ContractNumber': 5, 'WeeklyContractRate': 70, 'MinWeeklyHours': 20, 'OvertimeRatePerHour': 100, 'IsFullTime': False,
    'HospitalId': 10003,
}
DOCTOR_MODEL11 = {
    'DoctorId': 111, 'Name': 'Madison', 'OfficePhoneNumber': '6469297874', 'PersonalPhoneNumber': '(960) 240-5859', 'Specialty': 'Dental',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 400000, 'IsFullTime': True,
    'HospitalId': 10003,
}
DOCTOR_MODEL12 = {
    'DoctorId': 112, 'Name': 'Madison', 'OfficePhoneNumber': '6469297874', 'PersonalPhoneNumber': '(960) 240-5859', 'Specialty': 'Dental',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 350000, 'IsFullTime': True,
    'HospitalId': 10003,
}
DOCTOR_MODEL13 = {
    'DoctorId': 113, 'Name': 'Jay', 'OfficePhoneNumber': '6469297878', 'PersonalPhoneNumber': '(960) 240-5852', 'Specialty': 'Ophthalmology',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 400000, 'IsFullTime': True,
    'HospitalId': 10002,
}
DOCTOR_MODEL13 = {
    'DoctorId': 113, 'Name': 'Karen', 'OfficePhoneNumber': '6469297811', 'PersonalPhoneNumber': '(960) 240-5132', 'Specialty': 'Medical Clinic',
    'HireDate': '2020-10-01 08:00:00', 'YearlyCompensation': 500000, 'IsFullTime': True,
    'HospitalId': 10001,
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
    'ICD': 'R50', 'Description': 'Fever', 
    'Type': 'Seasonal', 'TableLastDate': '2021-11-09 14:46:05',
}
DISEASE_MODEL7 = {
    'DiseaseId': 207, 
    'ICD': 'R51', 'Description': 'Headache', 
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
DISEASE_MODEL11 = {
    'DiseaseId': 211, 
    'ICD': 'R51', 'Description': 'Flu', 
    'Type': 'Seasonal', 'TableLastDate': '2021-11-09 14:46:05',
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
           'EmergencyContact': 'John', 'IsInPatient': False, 'FollowUpDate': '2021-02-15 09:36:32',
           'TableLastDate': '2021-02-15 09:36:32'}

PATIENT_MODEL6 = {'PatientID': 6, 'Name': 'Leslie', 'Address': '70 Columbus Drive', 'PhoneNumber': '6549997164',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Kai', 'IsInPatient': True, 'FollowUpDate': '2021-10-21 11:05:46', 'BedNumber': 25,
           'Floor': 5,
           'DischargeDate': '2021-10-21 11:05:46', 'TableLastDate': '2021-10-21 11:05:46'}

PATIENT_MODEL7 = {'PatientID': 7, 'Name': 'Mila', 'Address': '475 Washington Street', 'PhoneNumber': '8412546184',
           'RelationshipWithEmergencyContact': 'Husband',
           'EmergencyContact': 'Jerry', 'IsInPatient': False, 'FollowUpDate': '2021-10-06 16:28:55', 
           'TableLastDate': '2021-10-06 16:28:55'}

PATIENT_MODEL8 = {'PatientID': 8, 'Name': 'Zion', 'Address': '475 Washington Street', 'PhoneNumber': '3467816455',
           'RelationshipWithEmergencyContact': 'Friend',
           'EmergencyContact': 'Bob', 'IsInPatient': False, 'FollowUpDate': '2021-10-08 11:28:12', 
           'TableLastDate': '2021-10-08 11:28:12'}

# Treatment Table
TREATMENT_MODEL1 = {'TreatmentId': 1, 'DoctorId': 101, 'TreatmentDate': '2021-12-01 16:28:55', 
           'RegistrationId': 1, 'DiseaseId': 211
}
TREATMENT_MODEL2 = {'TreatmentId': 2, 'DoctorId': 102, 'TreatmentDate': '2021-12-02 16:28:55', 
           'RegistrationId': 2, 'DiseaseId': 211
}
TREATMENT_MODEL3 = {'TreatmentId': 3, 'DoctorId': 103, 'TreatmentDate': '2021-12-03 16:28:55', 
           'RegistrationId': 3, 'DiseaseId': 207
}
TREATMENT_MODEL4 = {'TreatmentId': 4, 'DoctorId': 101, 'TreatmentDate': '2021-12-04 16:28:55', 
           'RegistrationId': 4, 'DiseaseId': 211
}
TREATMENT_MODEL5 = {'TreatmentId': 5, 'DoctorId': 102, 'TreatmentDate': '2021-12-04 16:28:55', 
           'RegistrationId': 5, 'DiseaseId': 211
}
TREATMENT_MODEL6 = {'TreatmentId': 6, 'DoctorId': 103, 'TreatmentDate': '2021-12-05 16:28:55', 
           'RegistrationId': 6, 'DiseaseId': 211
}
TREATMENT_MODEL7 = {'TreatmentId': 7, 'DoctorId': 101, 'TreatmentDate': '2021-12-05 16:28:55', 
           'RegistrationId': 7, 'DiseaseId': 211
}
TREATMENT_MODEL8 = {'TreatmentId': 8, 'DoctorId': 102, 'TreatmentDate': '2021-12-05 16:28:55', 
           'RegistrationId': 8, 'DiseaseId': 211
}
TREATMENT_MODEL9 = {'TreatmentId': 9, 'DoctorId': 110, 'TreatmentDate': '2021-12-06 16:28:55', 
           'RegistrationId': 9, 'DiseaseId': 204
}
TREATMENT_MODEL10 = {'TreatmentId': 10, 'DoctorId': 102, 'TreatmentDate': '2021-12-07 16:28:55', 
           'RegistrationId': 10, 'DiseaseId': 211
}
TREATMENT_MODEL11 = {'TreatmentId': 11, 'DoctorId': 101, 'TreatmentDate': '2021-11-07 16:28:55', 
           'RegistrationId': 11, 'DiseaseId': 206
}
TREATMENT_MODEL12 = {'TreatmentId': 12, 'DoctorId': 101, 'TreatmentDate': '2021-11-08 16:28:55', 
           'RegistrationId': 12, 'DiseaseId': 206
}
TREATMENT_MODEL13 = {'TreatmentId': 13, 'DoctorId': 101, 'TreatmentDate': '2021-11-09 16:28:55', 
           'RegistrationId': 13, 'DiseaseId': 206
}
TREATMENT_MODEL14 = {'TreatmentId': 14, 'DoctorId': 101, 'TreatmentDate': '2021-11-10 16:28:55', 
           'RegistrationId': 14, 'DiseaseId': 206
}
TREATMENT_MODEL15 = {'TreatmentId': 15, 'DoctorId': 103, 'TreatmentDate': '2021-09-03 16:28:55', 
           'RegistrationId': 15, 'DiseaseId': 204
}
TREATMENT_MODEL16 = {'TreatmentId': 16, 'DoctorId': 103, 'TreatmentDate': '2021-09-04 16:28:55', 
           'RegistrationId': 16, 'DiseaseId': 204
}
TREATMENT_MODEL17 = {'TreatmentId': 17, 'DoctorId': 101, 'TreatmentDate': '2021-08-04 16:28:55', 
           'RegistrationId': 17, 'DiseaseId': 207
}
TREATMENT_MODEL18 = {'TreatmentId': 18, 'DoctorId': 101, 'TreatmentDate': '2021-08-05 16:28:55', 
           'RegistrationId': 18, 'DiseaseId': 207
}
TREATMENT_MODEL19 = {'TreatmentId': 19, 'DoctorId': 101, 'TreatmentDate': '2021-08-06 16:28:55', 
           'RegistrationId': 19, 'DiseaseId': 207
}
TREATMENT_MODEL20 = {'TreatmentId': 20, 'DoctorId': 107, 'TreatmentDate': '2021-07-06 16:28:55', 
           'RegistrationId': 20, 'DiseaseId': 208
}

# Registration Table
REGISTRATION_MODEL1 = {'RegistrationID': 1, 'RegistrationDate': '2021-12-01 16:28:55', 'RegistrationNumber': '1',
           'PatientId': 1,  'TableLastDate': '2021-12-01 16:28:55', 'HasProcessed': True, 'TreatmentId': 1, 
}
REGISTRATION_MODEL2 = {'RegistrationID': 2, 'RegistrationDate': '2021-12-02 16:28:55', 'RegistrationNumber': '2',
           'PatientId': 2,  'TableLastDate': '2021-12-02 16:28:55', 'HasProcessed': True, 'TreatmentId': 2, 
}
REGISTRATION_MODEL3 = {'RegistrationID': 3, 'RegistrationDate': '2021-12-03 16:28:55', 'RegistrationNumber': '3',
           'PatientId': 3,  'TableLastDate': '2021-12-03 16:28:55', 'HasProcessed': True, 'TreatmentId': 3, 
}
REGISTRATION_MODEL4 = {'RegistrationID': 4, 'RegistrationDate': '2021-12-04 16:28:55', 'RegistrationNumber': '4',
           'PatientId': 1,  'TableLastDate': '2021-12-04 16:28:55', 'HasProcessed': True, 'TreatmentId': 4, 
}
REGISTRATION_MODEL5 = {'RegistrationID': 5, 'RegistrationDate': '2021-12-04 16:28:55', 'RegistrationNumber': '5',
           'PatientId': 4,  'TableLastDate': '2021-12-04 16:28:55', 'HasProcessed': True, 'TreatmentId': 5, 
}
REGISTRATION_MODEL6 = {'RegistrationID': 6, 'RegistrationDate': '2021-12-05 16:28:55', 'RegistrationNumber': '6',
           'PatientId': 5,  'TableLastDate': '2021-12-05 16:28:55', 'HasProcessed': True, 'TreatmentId': 6, 
}
REGISTRATION_MODEL7 = {'RegistrationID': 7, 'RegistrationDate': '2021-12-05 16:28:55', 'RegistrationNumber': '7',
           'PatientId': 1,  'TableLastDate': '2021-12-05 16:28:55', 'HasProcessed': True, 'TreatmentId': 7, 
}
REGISTRATION_MODEL8 = {'RegistrationID': 8, 'RegistrationDate': '2021-12-05 16:28:55', 'RegistrationNumber': '8',
           'PatientId': 2,  'TableLastDate': '2021-12-05 16:28:55', 'HasProcessed': True, 'TreatmentId': 8, 
}
REGISTRATION_MODEL9 = {'RegistrationID': 9, 'RegistrationDate': '2021-12-06 16:28:55', 'RegistrationNumber': '9',
           'PatientId': 6,  'TableLastDate': '2021-12-06 16:28:55', 'HasProcessed': True, 'TreatmentId': 9, 
}
REGISTRATION_MODEL10 = {'RegistrationID': 10, 'RegistrationDate': '2021-12-07 16:28:55', 'RegistrationNumber': '10',
           'PatientId': 2,  'TableLastDate': '2021-12-07 16:28:55', 'HasProcessed': True, 'TreatmentId': 10, 
}
REGISTRATION_MODEL11 = {'RegistrationID': 11, 'RegistrationDate': '2021-11-07 16:28:55', 'RegistrationNumber': '11',
           'PatientId': 1,  'TableLastDate': '2021-11-07 16:28:55', 'HasProcessed': True, 'TreatmentId': 11, 
}
REGISTRATION_MODEL12 = {'RegistrationID': 12, 'RegistrationDate': '2021-11-08 16:28:55', 'RegistrationNumber': '12',
           'PatientId': 2,  'TableLastDate': '2021-11-08 16:28:55', 'HasProcessed': True, 'TreatmentId': 12, 
}
REGISTRATION_MODEL13 = {'RegistrationID': 13, 'RegistrationDate': '2021-11-09 16:28:55', 'RegistrationNumber': '13',
           'PatientId': 3,  'TableLastDate': '2021-11-09 16:28:55', 'HasProcessed': True, 'TreatmentId': 13, 
}
REGISTRATION_MODEL14 = {'RegistrationID': 14, 'RegistrationDate': '2021-11-10 16:28:55', 'RegistrationNumber': '14',
           'PatientId': 4,  'TableLastDate': '2021-11-10 16:28:55', 'HasProcessed': True, 'TreatmentId': 14, 
}
REGISTRATION_MODEL15 = {'RegistrationID': 15, 'RegistrationDate': '2021-09-03 16:28:55', 'RegistrationNumber': '15',
           'PatientId': 5,  'TableLastDate': '2021-09-03 16:28:55', 'HasProcessed': True, 'TreatmentId': 15, 
}
REGISTRATION_MODEL16 = {'RegistrationID': 16, 'RegistrationDate': '2021-09-04 16:28:55', 'RegistrationNumber': '16',
           'PatientId': 6,  'TableLastDate': '2021-09-04 16:28:55', 'HasProcessed': True, 'TreatmentId': 16, 
}
REGISTRATION_MODEL17 = {'RegistrationID': 17, 'RegistrationDate': '2021-08-04 16:28:55', 'RegistrationNumber': '17',
           'PatientId': 7,  'TableLastDate': '2021-08-04 16:28:55', 'HasProcessed': True, 'TreatmentId': 17, 
}
REGISTRATION_MODEL18 = {'RegistrationID': 18, 'RegistrationDate': '2021-08-05 16:28:55', 'RegistrationNumber': '18',
           'PatientId': 8,  'TableLastDate': '2021-08-05 16:28:55', 'HasProcessed': True, 'TreatmentId': 18, 
}
REGISTRATION_MODEL19 = {'RegistrationID': 19, 'RegistrationDate': '2021-08-06 16:28:55', 'RegistrationNumber': '19',
           'PatientId': 1,  'TableLastDate': '2021-08-06 16:28:55', 'HasProcessed': True, 'TreatmentId': 19, 
}
REGISTRATION_MODEL20 = {'RegistrationID': 20, 'RegistrationDate': '2021-07-06 16:28:55', 'RegistrationNumber': '20',
           'PatientId': 2,  'TableLastDate': '2021-07-06 16:28:55', 'HasProcessed': True, 'TreatmentId': 20, 
}

# Payment Table
PAYMENT_MODEL1 = {'PaymentId': 1, 'RegistrationDate': '2021-12-01 16:28:55', 'Type': 'Credit Card',
           'Amount': 320, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 1, 
           'PatientId': 1, 'InvoiceId': 1
}
PAYMENT_MODEL2 = {'PaymentId': 2, 'RegistrationDate': '2021-12-02 16:28:55', 'Type': 'Credit Card',
           'Amount': 55, 'TableLastDate': '2021-12-02 16:28:55', 'RegistrationId': 2, 
           'PatientId': 2, 'InvoiceId': 2
}
PAYMENT_MODEL3 = {'PaymentId': 3, 'RegistrationDate': '2021-12-03 16:28:55', 'Type': 'Cash',
           'Amount': 550, 'TableLastDate': '2021-12-03 16:28:55', 'RegistrationId': 3, 
           'PatientId': 3, 'InvoiceId': 3
}
PAYMENT_MODEL4 = {'PaymentId': 4, 'RegistrationDate': '2021-12-04 16:28:55', 'Type': 'Credit Card',
           'Amount': 120, 'TableLastDate': '2021-12-04 16:28:55', 'RegistrationId': 4, 
           'PatientId': 1, 'InvoiceId': 4
}
PAYMENT_MODEL5 = {'PaymentId': 5, 'RegistrationDate': '2021-12-04 16:28:55', 'Type': 'Cash',
           'Amount': 90, 'TableLastDate': '2021-12-04 16:28:55', 'RegistrationId': 5, 
           'PatientId': 4, 'InvoiceId': 5
}
PAYMENT_MODEL6 = {'PaymentId': 6, 'RegistrationDate': '2021-12-05 16:28:55', 'Type': 'Credit Card',
           'Amount': 95, 'TableLastDate': '2021-12-05 16:28:55', 'RegistrationId': 6, 
           'PatientId': 5, 'InvoiceId': 6
}
PAYMENT_MODEL7 = {'PaymentId': 7, 'RegistrationDate': '2021-12-05 16:28:55', 'Type': 'Credit Card',
           'Amount': 225, 'TableLastDate': '2021-12-05 16:28:55', 'RegistrationId': 7, 
           'PatientId': 1, 'InvoiceId': 7
}
PAYMENT_MODEL8 = {'PaymentId': 8, 'RegistrationDate': '2021-12-05 16:28:55', 'Type': 'Cash',
           'Amount': 80, 'TableLastDate': '2021-12-05 16:28:55', 'RegistrationId': 8, 
           'PatientId': 2, 'InvoiceId': 8
}
PAYMENT_MODEL9 = {'PaymentId': 9, 'RegistrationDate': '2021-12-06 16:28:55', 'Type': 'Credit Card',
           'Amount': 400, 'TableLastDate': '2021-12-06 16:28:55', 'RegistrationId': 9, 
           'PatientId': 6, 'InvoiceId': 9
}
PAYMENT_MODEL10 = {'PaymentId': 10, 'RegistrationDate': '2021-12-07 16:28:55', 'Type': 'Credit Card',
           'Amount': 10, 'TableLastDate': '2021-12-07 16:28:55', 'RegistrationId': 10, 
           'PatientId': 2, 'InvoiceId': 10
}
PAYMENT_MODEL11 = {'PaymentId': 11, 'RegistrationDate': '2021-11-07 16:28:55', 'Type': 'Credit Card',
           'Amount': 320, 'TableLastDate': '2021-11-07 16:28:55', 'RegistrationId': 11, 
           'PatientId': 1, 'InvoiceId': 11
}
PAYMENT_MODEL12 = {'PaymentId': 12, 'RegistrationDate': '2021-11-08 16:28:55', 'Type': 'Credit Card',
           'Amount': 55, 'TableLastDate': '2021-11-08 16:28:55', 'RegistrationId': 12, 
           'PatientId': 2, 'InvoiceId': 12
}
PAYMENT_MODEL13 = {'PaymentId': 13, 'RegistrationDate': '2021-11-09 16:28:55', 'Type': 'Cash',
           'Amount': 550, 'TableLastDate': '2021-11-09 16:28:55', 'RegistrationId': 13, 
           'PatientId': 3, 'InvoiceId': 13
}
PAYMENT_MODEL14 = {'PaymentId': 14, 'RegistrationDate': '2021-11-10 16:28:55', 'Type': 'Credit Card',
           'Amount': 120, 'TableLastDate': '2021-11-10 16:28:55', 'RegistrationId': 14, 
           'PatientId': 4, 'InvoiceId': 14
}
PAYMENT_MODEL15 = {'PaymentId': 15, 'RegistrationDate': '2021-09-03 16:28:55', 'Type': 'Cash',
           'Amount': 90, 'TableLastDate': '2021-09-03 16:28:55', 'RegistrationId': 15, 
           'PatientId': 5, 'InvoiceId': 15
}
PAYMENT_MODEL16 = {'PaymentId': 16, 'RegistrationDate': '2021-09-04 16:28:55', 'Type': 'Credit Card',
           'Amount': 95, 'TableLastDate': '2021-09-04 16:28:55', 'RegistrationId': 16, 
           'PatientId': 6, 'InvoiceId': 16
}
PAYMENT_MODEL17 = {'PaymentId': 17, 'RegistrationDate': '2021-08-04 16:28:55', 'Type': 'Credit Card',
           'Amount': 225, 'TableLastDate': '2021-08-04 16:28:55', 'RegistrationId': 17, 
           'PatientId': 7, 'InvoiceId': 17
}
PAYMENT_MODEL18 = {'PaymentId': 18, 'RegistrationDate': '2021-08-05 16:28:55', 'Type': 'Cash',
           'Amount': 80, 'TableLastDate': '2021-08-05 16:28:55', 'RegistrationId': 18, 
           'PatientId': 8, 'InvoiceId': 18
}
PAYMENT_MODEL19 = {'PaymentId': 19, 'RegistrationDate': '2021-08-06 16:28:55', 'Type': 'Credit Card',
           'Amount': 400, 'TableLastDate': '2021-08-06 16:28:55', 'RegistrationId': 19, 
           'PatientId': 1, 'InvoiceId': 19
}
PAYMENT_MODEL20 = {'PaymentId': 20, 'RegistrationDate': '2021-07-06 16:28:55', 'Type': 'Credit Card',
           'Amount': 10, 'TableLastDate': '2021-07-06 16:28:55', 'RegistrationId': 20, 
           'PatientId': 2, 'InvoiceId': 20
}

# Invoice Table
INVOICE_MODEL1 = {'InvoiceId': 1, 'InvoiceNumber': '1', 'InvoiceDate': '2021-12-01 16:28:55',
           'LabCost': 200,  'DrugCost': 120, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 320, 
           'BillToInsurance': 320,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 1, 'PatientId': 1, 
}
INVOICE_MODEL2 = {'InvoiceId': 2, 'InvoiceNumber': '2', 'InvoiceDate': '2021-12-02 16:28:55',
           'LabCost': 0,  'DrugCost': 55, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 55, 
           'BillToInsurance': 55,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 2, 'PatientId': 2, 
}
INVOICE_MODEL3 = {'InvoiceId': 3, 'InvoiceNumber': '3', 'InvoiceDate': '2021-12-03 16:28:55',
           'LabCost': 200,  'DrugCost': 0, 'SurgeryCost': 350, 'BedUsageCost': 0, 'TotalCost': 550, 
           'BillToInsurance': 500,  'CostToPatient': 50, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 3, 'PatientId': 3, 
}
INVOICE_MODEL4 = {'InvoiceId': 4, 'InvoiceNumber': '4', 'InvoiceDate': '2021-12-04 16:28:55',
           'LabCost': 0,  'DrugCost': 120, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 120, 
           'BillToInsurance': 120,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 4, 'PatientId': 1, 
}
INVOICE_MODEL5 = {'InvoiceId': 5, 'InvoiceNumber': '5', 'InvoiceDate': '2021-12-04 16:28:55',
           'LabCost': 0,  'DrugCost': 90, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 90, 
           'BillToInsurance': 90,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 5, 'PatientId': 4, 
}
INVOICE_MODEL6 = {'InvoiceId': 6, 'InvoiceNumber': '6', 'InvoiceDate': '2021-12-05 16:28:55',
           'LabCost': 0,  'DrugCost': 95, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 95, 
           'BillToInsurance': 95,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 6, 'PatientId': 5, 
}
INVOICE_MODEL7 = {'InvoiceId': 7, 'InvoiceNumber': '7', 'InvoiceDate': '2021-12-05 16:28:55',
           'LabCost': 0,  'DrugCost': 225, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 225, 
           'BillToInsurance': 125,  'CostToPatient': 100, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 7, 'PatientId': 1, 
}
INVOICE_MODEL8 = {'InvoiceId': 8, 'InvoiceNumber': '8', 'InvoiceDate': '2021-12-05 16:28:55',
           'LabCost': 0,  'DrugCost': 80, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 80, 
           'BillToInsurance': 80,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 8, 'PatientId': 2, 
}
INVOICE_MODEL9 = {'InvoiceId': 9, 'InvoiceNumber': '9', 'InvoiceDate': '2021-12-06 16:28:55',
           'LabCost': 180,  'DrugCost': 20, 'SurgeryCost': 200, 'BedUsageCost': 0, 'TotalCost': 400, 
           'BillToInsurance': 100,  'CostToPatient': 300, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 9, 'PatientId': 6, 
}
INVOICE_MODEL10 = {'InvoiceId': 10, 'InvoiceNumber': '10', 'InvoiceDate': '2021-12-07 16:28:55',
           'LabCost': 0,  'DrugCost': 10, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 10, 
           'BillToInsurance': 10,  'CostToPatient': 0, 'TableLastDate': '2021-12-01 16:28:55', 'RegistrationId': 10, 'PatientId': 2, 
}
INVOICE_MODEL11 = {'InvoiceId': 11, 'InvoiceNumber': '11', 'InvoiceDate': '2021-11-07 16:28:55',
           'LabCost': 200,  'DrugCost': 120, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 320, 
           'BillToInsurance': 320,  'CostToPatient': 0, 'TableLastDate': '2021-11-07 16:28:55', 'RegistrationId': 11, 'PatientId': 1, 
}
INVOICE_MODEL12 = {'InvoiceId': 12, 'InvoiceNumber': '12', 'InvoiceDate': '2021-11-08 16:28:55',
           'LabCost': 0,  'DrugCost': 55, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 55, 
           'BillToInsurance': 55,  'CostToPatient': 0, 'TableLastDate': '2021-11-08 16:28:55', 'RegistrationId': 12, 'PatientId': 2, 
}
INVOICE_MODEL13 = {'InvoiceId': 13, 'InvoiceNumber': '13', 'InvoiceDate': '2021-11-09 16:28:55',
           'LabCost': 200,  'DrugCost': 0, 'SurgeryCost': 350, 'BedUsageCost': 0, 'TotalCost': 550, 
           'BillToInsurance': 500,  'CostToPatient': 50, 'TableLastDate': '2021-11-09 16:28:55', 'RegistrationId': 13, 'PatientId': 3, 
}
INVOICE_MODEL14 = {'InvoiceId': 14, 'InvoiceNumber': '14', 'InvoiceDate': '2021-11-10 16:28:55',
           'LabCost': 0,  'DrugCost': 120, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 120, 
           'BillToInsurance': 120,  'CostToPatient': 0, 'TableLastDate': '2021-11-10 16:28:55', 'RegistrationId': 14, 'PatientId': 4, 
}
INVOICE_MODEL15 = {'InvoiceId': 15, 'InvoiceNumber': '15', 'InvoiceDate': '2021-09-03 16:28:55',
           'LabCost': 0,  'DrugCost': 90, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 90, 
           'BillToInsurance': 90,  'CostToPatient': 0, 'TableLastDate': '2021-09-03 16:28:55', 'RegistrationId': 15, 'PatientId': 5, 
}
INVOICE_MODEL16 = {'InvoiceId': 16, 'InvoiceNumber': '16', 'InvoiceDate': '2021-09-04 16:28:55',
           'LabCost': 0,  'DrugCost': 95, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 95, 
           'BillToInsurance': 95,  'CostToPatient': 0, 'TableLastDate': '2021-09-04 16:28:55', 'RegistrationId': 16, 'PatientId': 6, 
}
INVOICE_MODEL17 = {'InvoiceId': 17, 'InvoiceNumber': '17', 'InvoiceDate': '2021-08-04 16:28:55',
           'LabCost': 0,  'DrugCost': 225, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 225, 
           'BillToInsurance': 125,  'CostToPatient': 100, 'TableLastDate': '2021-08-04 16:28:55', 'RegistrationId': 17, 'PatientId': 7, 
}
INVOICE_MODEL18 = {'InvoiceId': 18, 'InvoiceNumber': '18', 'InvoiceDate': '2021-08-05 16:28:55',
           'LabCost': 0,  'DrugCost': 80, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 80, 
           'BillToInsurance': 80,  'CostToPatient': 0, 'TableLastDate': '2021-08-05 16:28:55', 'RegistrationId': 18, 'PatientId': 8, 
}
INVOICE_MODEL19 = {'InvoiceId': 19, 'InvoiceNumber': '19', 'InvoiceDate': '2021-08-06 16:28:55',
           'LabCost': 180,  'DrugCost': 20, 'SurgeryCost': 200, 'BedUsageCost': 0, 'TotalCost': 400, 
           'BillToInsurance': 100,  'CostToPatient': 300, 'TableLastDate': '2021-08-06 16:28:55', 'RegistrationId': 19, 'PatientId': 1, 
}
INVOICE_MODEL20 = {'InvoiceId': 20, 'InvoiceNumber': '20', 'InvoiceDate': '2021-07-06 16:28:55',
           'LabCost': 0,  'DrugCost': 10, 'SurgeryCost': 0, 'BedUsageCost': 0, 'TotalCost': 10, 
           'BillToInsurance': 10,  'CostToPatient': 0, 'TableLastDate': '2021-07-06 16:28:55', 'RegistrationId': 20, 'PatientId': 2, 
}
