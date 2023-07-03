CREATE TABLE IF NOT EXISTS `Provider` (
  `ProviderKey` varchar(20) NOT NULL,
  `FirstName` varchar(60) NOT NULL,
  `LastName` varchar(60) NOT NULL,
  `NPI` varchar(10) NOT NULL,
  PRIMARY KEY (`ProviderKey`)
);

