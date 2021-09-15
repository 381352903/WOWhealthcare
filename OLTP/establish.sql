CREATE TABLE IF NOT EXISTS `patient`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `Address` VARCHAR(255),
   `PhoneNumber` VARCHAR(255),
   `RelationshipWithEmergencyContact` VARCHAR(255),
   `EmergencyContact` VARCHAR(255),
   `IsInPatient` BOOLEAN,
   `FollowUpDate` DATETIME,
   `BedNumber` INTEGER,
   `Floor` INTEGER,
   `DischargeDate` DATETIME,
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doctor`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `OfficePhoneNumber` VARCHAR(255),
   `PersonalPhoneNumber` VARCHAR(255),
   `Specialty` VARCHAR(255),
   `HireDate` DATETIME,
   `YearlyCompensation` INTEGER,
   `ContractDate` DATETIME,
   `ContractNumber` INTEGER,
   `WeeklyContractRate` INTEGER,
   `MinWeeklyHours` INTEGER,
   `OvertimeRatePerHour` INTEGER,
   `IsFullTime` BOOLEAN,
   `TableLastDate` DATETIME,
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
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `treatment`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `TreatmentDate` DATETIME,
   `TreatmentType` VARCHAR(255),
   `ResultStatus` VARCHAR(255),
   `Description` VARCHAR(255),
   `LabName` VARCHAR(255),
   `TestType` VARCHAR(255),
   `TestDate` DATETIME,
   `TestResult` VARCHAR(255),
   `DrugName` VARCHAR(255),
   `DrugDose` VARCHAR(255),
   `SurgeryName` VARCHAR(255),
   `SurgeryDescription` VARCHAR(255),
   `SurgeryDate` DATETIME,
   `SurgeryResult` VARCHAR(255),
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `disease`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `ICD` INTEGER,
   `Discerption` VARCHAR(255),
   `Type` VARCHAR(255),
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `registration`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `RegistrationDate` DATETIME,
   `RegistrationNumber` VARCHAR(255),
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `invoice`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `InvoiceNumber` INTEGER,
   `InvoiceDate` DATETIME,
   `LabCost` VARCHAR(255),
   `DrugCost` VARCHAR(255),
   `SurgeryCost` VARCHAR(255),
   `BedUsageCost` VARCHAR(255),
   `TotalCost` VARCHAR(255),
   `BillToInsurance` VARCHAR(255),
   `CostToPatient` VARCHAR(255),
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `payment`(
   `Id` INT UNSIGNED AUTO_INCREMENT,
   `PaymentDate` DATETIME,
   `Amount` INTEGER,
   `TableLastDate` DATETIME,
   PRIMARY KEY ( `Id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doctor_disease`(
   `DoctorId` INT UNSIGNED,
   `DiseaseId` INT UNSIGNED,
   `TableLastDate` DATETIME
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patient_doctor`(
   `PatientId` INT UNSIGNED,
   `DoctorId` INT UNSIGNED,
   `TableLastDate` DATETIME
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `patient_treatment`(
   `PatientId` INT UNSIGNED,
   `TreatmentId` INT UNSIGNED,
   `TableLastDate` DATETIME
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

