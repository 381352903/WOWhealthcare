CREATE TABLE IF NOT EXISTS `patient`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `Address` VARCHAR(255),
   `PhoneNumber` VARCHAR(255),
   `RelationshipWithEmergencyContact` VARCHAR(255),
   `EmergencyContact` VARCHAR(255),
   `IsInPatient` BOOLEAN,
   `FollowUpDate` DATE,
   `BedNumber` INTEGER,
   `Floor` INTEGER,
   `DischargeDate` DATE,
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doctor`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `OfficePhoneNumber` VARCHAR(255),
   `PersonalPhoneNumber` VARCHAR(255),
   `Specialty` VARCHAR(255),
   `HireDate` DATE,
   `YearlyCompensation` INTEGER,
   `ContractDate` DATE,
   `ContractNumber` INTEGER,
   `WeeklyContractRate` INTEGER,
   `MinWeeklyHours` INTEGER,
   `OvertimeRatePerHour` INTEGER,
   `IsFullTime` BOOLEAN,
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `hospital`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `Address` VARCHAR(255),
   `Specialty` VARCHAR(255),
   `EmergencyHotlineNumbers` VARCHAR(255),
   `GeneralInquiryPhoneNumbers` VARCHAR(255),
   `RegistrationNumber` VARCHAR(255),
   `DepartmentNames` VARCHAR(255),
   `DepartmentLocation` VARCHAR(255),
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `treatment`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `TreatmentDate` DATE,
   `TreatmentType` VARCHAR(255),
   `ResultStatus` VARCHAR(255),
   `Description` VARCHAR(255),
   `LabName` VARCHAR(255),
   `TestType` VARCHAR(255),
   `TestDate` VARCHAR(255),
   `TestResult` VARCHAR(255),
   `DrugName` VARCHAR(255),
   `DrugDose` VARCHAR(255),
   `SurgeryName` VARCHAR(255),
   `SurgeryDescription` VARCHAR(255),
   `SurgeryDate` VARCHAR(255),
   `SurgeryResult` VARCHAR(255),
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `disease`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `ICD` INTEGER,
   `Discerption` VARCHAR(255),
   `Type` VARCHAR(255),
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `registration`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `RegistrationDate` DATE,
   `RegistrationNumber` VARCHAR(255),
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `invoice`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `InvoiceNumber` DATE,
   `InvoiceDate` VARCHAR(255),
   `LabCost` VARCHAR(255),
   `DrugCost` VARCHAR(255),
   `SurgeryCost` VARCHAR(255),
   `BedUsageCost` VARCHAR(255),
   `TotalCost` VARCHAR(255),
   `BillToInsurance` VARCHAR(255),
   `CostToPatient` VARCHAR(255),
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `payment`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `PaymentDate` DATE,
   `Amount` INTEGER,
   `TableLastDate` DATE,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doctor_disease`(
   `DoctorId` INT UNSIGNED,
   `DiseaseId` INT UNSIGNED,
   `TableLastDate` DATE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patient_doctor`(
   `PatientId` INT UNSIGNED,
   `DoctorId` INT UNSIGNED,
   `TableLastDate` DATE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patient_treatment`(
   `PatientId` INT UNSIGNED,
   `TreatmentId` INT UNSIGNED,
   `TableLastDate` DATE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

