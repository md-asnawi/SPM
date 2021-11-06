CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `employee`;

CREATE TABLE IF NOT EXISTS `employee` (
  `employee_name` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `current_designation` VARCHAR(45) NOT NULL,
  `department` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`username`)
);

INSERT INTO `employee` (`employee_name`, `username`, `current_designation`, `department`) VALUES
('Tom Tan', 'tomtan.2016', 'Senior Engineer', 'Ink'),
('Dick Lin', 'dicklin.2019', 'Junior Engineer', 'Printer'),
('Harry Wu', 'harrywu.2017', 'Senior Engineer', 'Data'),
('Jack Sivam', 'jacksivam.2018', 'Senior Engineer', 'Design'),
('Sam Koh', 'samkoh.2021', 'Junior Engineer', 'Ink');
