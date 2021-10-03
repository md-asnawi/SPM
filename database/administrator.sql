CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `administrator`;

CREATE TABLE IF NOT EXISTS `administrator` (
  `administrator_id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`administrator_id`)
);

INSERT INTO `administrator` (`administrator_id`, `name`) VALUES
('1', 'Amber'),
('2', 'Pearl'),
('3', 'Kris'),
('4', 'Bala'),
('5', 'Donovan');
