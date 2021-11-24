use WOW;

SELECT
Name,
HospitalId
FROM hospital
INTO OUTFILE '/Users/abc/Desktop/shared/test.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

SELECT
patient.Name,
patient.IsInPatient,
doctor.Name,
doctor.Specialty,
hospital.Name,
hospital.Address,
disease.Type,
treatment.TreatmentDate,
treatment.Description,
treatment.TreatmentType,
treatment.ResultStatus,
invoice.InvoiceId
FROM treatment
LEFT JOIN registration
ON treatment.RegistrationId = registration.RegistrationId
LEFT JOIN patient
ON registration.PatientId = patient.PatientId
LEFT JOIN doctor
ON treatment.DoctorId = doctor.DoctorId
LEFT JOIN hospital
ON doctor.HospitalId = hospital.HospitalId
LEFT JOIN disease
ON treatment.DiseaseId = disease.DiseaseId
LEFT JOIN invoice
ON registration.RegistrationId = invoice.RegistrationId
WHERE treatment.TableLastDate > date_sub(curdate(),interval 1 day)
INTO OUTFILE '/Users/abc/Desktop/shared/dw_fact.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '"'
LINES TERMINATED BY '\r\n';
