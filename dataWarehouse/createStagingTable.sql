drop table STG_FACT;

CREATE TABLE STG_FACT (
    fact_id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
    patient_name VARCHAR2(255),
    doctor_name VARCHAR2(255),
    doctor_specialty VARCHAR2(255),
    hospital_name VARCHAR2(255),
    hospital_location VARCHAR2(255),
    disease_type VARCHAR2(255),
    treatment_date DATE,
    treatment_description VARCHAR2(255),
    treatment_type VARCHAR2(255),
    treatment_result VARCHAR2(255),
    invoice_id NUMBER,
    is_patient_in_hospital NUMBER(1)
);

CREATE TABLE DW_FACT (
    fact_id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
    patient_name VARCHAR2(255),
    doctor_name VARCHAR2(255),
    doctor_specialty VARCHAR2(255),
    hospital_name VARCHAR2(255),
    hospital_location VARCHAR2(255),
    disease_type VARCHAR2(255),
    treatment_date DATE,
    treatment_description VARCHAR2(255),
    treatment_type VARCHAR2(255),
    treatment_result VARCHAR2(255),
    invoice_id NUMBER,
    is_patient_in_hospital NUMBER(1)
);