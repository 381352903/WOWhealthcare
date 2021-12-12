create or replace PROCEDURE  load_dw_fact IS
dcnt NUMBER;
icnt NUMBER;
err_code NUMBER;
err_msg VARCHAR2(32000);
BEGIN
dcnt := 0;
icnt := 0;
for c in (select * from STG_FACT)
loop
    delete from DW_FACT where fact_id=c.fact_id and patient_name=c.patient_name;
    dcnt := dcnt+1;
     INSERT INTO DW_FACT  (fact_id,patient_name,doctor_name,doctor_specialty,hospital_name,hospital_location,disease_type,treatment_date,treatment_description,treatment_type,treatment_result,invoice_id,is_patient_in_hospital)
     VALUES (c.fact_id,c.patient_name,c.doctor_name,c.doctor_specialty,c.hospital_name,c.hospital_location,c.disease_type,c.treatment_date,c.treatment_description,c.treatment_type,c.treatment_result,c.invoice_id,c.is_patient_in_hospital);
     icnt := icnt+1;
     commit;
     dbms_output.put_line('Total Deleted Record: '||dcnt||' Total Inserted Records: '||icnt);
end loop;
     commit;
     dbms_output.put_line('Total Deleted Record: '||dcnt||' Total Inserted Records: '||icnt);
EXCEPTION
    WHEN OTHERS THEN
         err_code := SQLCODE;
         err_msg  := SQLERRM;
         dbms_output.put_line('Error code ' || err_code || ': ' || err_msg);
END;
/

CALL load_dw_fact();

=======

create or replace PROCEDURE  load_merge_dw_fact IS
err_code NUMBER;
err_msg VARCHAR2(32000);
BEGIN
    MERGE INTO DW_FACT e
    USING STG_FACT s
    ON (e.fact_id=s.fact_id AND e.patient_name=s.patient_name)
  WHEN MATCHED THEN
    UPDATE SET
         e.fact_id=s.fact_id,
         e.patient_name=s.patient_name,
         e.doctor_name=s.doctor_name,
         e.doctor_specialty=s.doctor_specialty,
         e.hospital_name=s.hospital_name,
         e.hospital_location=s.hospital_location,
         e.disease_type=s.disease_type,
         e.treatment_date=s.treatment_date,
         e.treatment_description=s.treatment_description,
         e.treatment_type=s.treatment_type,
         e.treatment_result=s.treatment_result,
         e.invoice_id=s.invoice_id,
         e.is_patient_in_hospital=s.is_patient_in_hospital
  WHEN NOT MATCHED THEN
      INSERT (fact_id,patient_name,doctor_name,doctor_specialty,hospital_name,hospital_location,disease_type,treatment_date,treatment_description,treatment_type,treatment_result,invoice_id,is_patient_in_hospital)
      VALUES (s.fact_id,s.patient_name,s.doctor_name,s.doctor_specialty,s.hospital_name,s.hospital_location,s.disease_type,s.treatment_date,s.treatment_description,s.treatment_type,s.treatment_result,s.invoice_id,s.is_patient_in_hospital);
      commit;
EXCEPTION
    WHEN OTHERS THEN
         err_code := SQLCODE;
         err_msg  := SQLERRM;
         dbms_output.put_line('Error code ' || err_code || ': ' || err_msg);
END;
/

CALL load_merge_dw_fact();