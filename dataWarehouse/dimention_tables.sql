CREATE TABLE ot.patient_request_fact (
    fact_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    patient_name VARCHAR2(255) NOT NULL,
    doctor_name VARCHAR2(255) NOT NULL,
    doctor_specialty VARCHAR2(255),
    hospital_name VARCHAR2(255) NOT NULL,
    hospital_location VARCHAR2(255),
    disease_type VARCHAR2(255) NOT NULL,
    treatment_date DATE NOT NULL,
    treatment_description VARCHAR2(255),
    treatment_type VARCHAR2(255),
    treatment_result VARCHAR2(255),
    invoice_id NUMBER NOT NULL,
    is_patient_in_hospital NUMBER(1) NOT NULL,
    PRIMARY KEY(fact_id)
);

CREATE TABLE ot.invoice(
    invoice_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    invoice_number NUMBER,
    invoice_date DATE,
    lab_cost NUMBER,
    drug_cost NUMBER,
    surgery_cost NUMBER,
    bed_usage_cost NUMBER,
    total_cost NUMBER NOT NULL,
    bill_to_insurance NUMBER,
    cost_to_patient NUMBER,
    PRIMARY KEY(invoice_id)
);

CREATE TABLE ot.payment(
    payment_id NUMBER GENERATED BY DEFAULT AS IDENTITY,
    payment_date DATE NOT NULL,
    amount NUMBER NOT NULL,
    type VARCHAR2(255) NOT NULL,
    invoice_id NUMBER NOT NULL,
    PRIMARY KEY(payment_id)
);

