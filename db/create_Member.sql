CREATE TABLE IF NOT EXISTS `Member` (
  `MemberKey` varchar(20) NOT NULL,
  `FirstName` varchar(60) NOT NULL,
  `LastName` varchar(60) NOT NULL,
  `DOB` date NOT NULL,
  PRIMARY KEY (`MemberKey`)
);