CREATE TABLE IF NOT EXISTS `patient`(
   `PatientId` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `Name` VARCHAR(255) NOT NULL,
   `Address` VARCHAR(255) NOT NULL,
   `PhoneNumber` VARCHAR(255) NOT NULL,
   `RelationshipWithEmergencyContact` VARCHAR(255) NOT NULL,
   `EmergencyContact` VARCHAR(255) NOT NULL,
   `IsInPatient` BOOLEAN NOT NULL,
   `FollowUpDate` DATETIME,
   `BedNumber` INTEGER,
   `Floor` INTEGER,
   `DischargeDate` DATETIME,
   `TableLastDate` DATETIME NOT NULL,
   `HospitalId` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `PatientId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `doctor`(
   `DoctorId` INT UNSIGNED AUTO_INCREMENT NOT NULL,
   `Name` VARCHAR(255) NOT NULL,
   `OfficePhoneNumber` VARCHAR(255),
   `PersonalPhoneNumber` VARCHAR(255) NOT NULL,
   `Specialty` VARCHAR(255) NOT NULL,
   `HireDate` DATETIME NOT NULL,
   `YearlyCompensation` INTEGER NOT NULL,
   `ContractDate` DATETIME NOT NULL,
   `ContractNumber` INTEGER,
   `WeeklyContractRate` INTEGER,
   `MinWeeklyHours` INTEGER,
   `OvertimeRatePerHour` INTEGER,
   `IsFullTime` BOOLEAN NOT NULL,
   `TableLastDate` DATETIME NOT NULL,
   `HospitalId` INTEGER NOT NULL,
   PRIMARY KEY ( `DoctorId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `hospital`(
   `HospitalId` INT UNSIGNED AUTO_INCREMENT,
   `Name` VARCHAR(255) NOT NULL,
   `Address` VARCHAR(255) NOT NULL,
   `Specialty` VARCHAR(255) NOT NULL,
   `EmergencyHotlineNumbers` VARCHAR(255),
   `GeneralInquiryPhoneNumbers` VARCHAR(255),
   `RegistrationNumber` VARCHAR(255),
   `DepartmentNames` VARCHAR(255),
   `DepartmentLocation` VARCHAR(255),
   `TableLastDate` DATETIME NOT NULL,
   PRIMARY KEY ( `HospitalId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `treatment`(
   `TreatmentId` INT UNSIGNED AUTO_INCREMENT,
   `DoctorId` INT UNSIGNED NOT NULL,
   `TreatmentDate` DATETIME NOT NULL,
   `TreatmentType` VARCHAR(255) NOT NULL,
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
   `RegistrationId` INT UNSIGNED NOT NULL,
   `DiseaseId` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `TreatmentId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `disease`(
   `DiseaseId` INT UNSIGNED AUTO_INCREMENT,
   `ICD` INTEGER NOT NULL,
   `Discerption` VARCHAR(255) NOT NULL,
   `Type` VARCHAR(255) NOT NULL,
   `TableLastDate` DATETIME NOT NULL,
   PRIMARY KEY ( `DiseaseId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `registration`(
   `RegistrationId` INT UNSIGNED AUTO_INCREMENT,
   `RegistrationDate` DATETIME NOT NULL,
   `RegistrationNumber` VARCHAR(255) NOT NULL,
   `PatientId` INT UNSIGNED NOT NULL,
   `TableLastDate` DATETIME NOT NULL,
   `HasProcessed` BOOLEAN NOT NULL,
   `TreatmentId` INTEGER NOT NULL DEFAULT 0,
   PRIMARY KEY ( `RegistrationId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `invoice`(
   `InvoiceId` INT UNSIGNED AUTO_INCREMENT,
   `InvoiceNumber` INTEGER NOT NULL,
   `InvoiceDate` DATETIME NOT NULL,
   `LabCost` INTEGER DEFAULT 0 NOT NULL,
   `DrugCost` INTEGER DEFAULT 0 NOT NULL,
   `SurgeryCost` INTEGER DEFAULT 0 NOT NULL,
   `BedUsageCost` INTEGER DEFAULT 0 NOT NULL,
   `TotalCost` INTEGER DEFAULT 0 NOT NULL,
   `BillToInsurance` INTEGER DEFAULT 0 NOT NULL,
   `CostToPatient` INTEGER DEFAULT 0 NOT NULL,
   `TableLastDate` DATETIME NOT NULL,
   `RegistrationId` INT UNSIGNED NOT NULL,
   `PatientId` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `InvoiceId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `payment`(
   `PaymentId` INT UNSIGNED AUTO_INCREMENT,
   `PaymentDate` DATETIME NOT NULL,
   `Type` VARCHAR(255) NOT NULL,
   `Amount` INTEGER DEFAULT 0 NOT NULL,
   `TableLastDate` DATETIME NOT NULL,
   `RegistrationId` INT UNSIGNED NOT NULL,
   `PatientId` INT UNSIGNED NOT NULL,
   `InvoiceId` INT UNSIGNED NOT NULL,
   PRIMARY KEY ( `PaymentId` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


