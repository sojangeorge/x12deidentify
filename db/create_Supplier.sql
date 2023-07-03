CREATE TABLE IF NOT EXISTS `Supplier` (
  `SupplierKey` varchar(20) NOT NULL,
  `Name` varchar(60) NOT NULL,
  `NPI` varchar(10) NOT NULL,
  `EIN` varchar(20) DEFAULT NULL,
  `TaxonomyCode` varchar(20) DEFAULT NULL,
  `MailingStreet1` varchar(60) DEFAULT NULL,
  `MailingStreet2` varchar(60) DEFAULT NULL,
  `MailingCity` varchar(40) DEFAULT NULL,
  `MailingState` varchar(10) DEFAULT NULL,
  `MailingZip` varchar(10) DEFAULT NULL,
  `BillingAddress1` varchar(60) DEFAULT NULL,
  `BillingAddress2` varchar(60) DEFAULT NULL,
  `BillingCity` varchar(40) DEFAULT NULL,
  `BillingState` varchar(10) DEFAULT NULL,
  `BillingZip` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`SupplierKey`)
);