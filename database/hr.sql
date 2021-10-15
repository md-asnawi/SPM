CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `hr`;

CREATE TABLE IF NOT EXISTS `hr` (
  `hr_id` INT NOT NULL,
  `hr_name` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`hr_id`));

INSERT INTO `hr` (`hr_id`, `hr_name`, `password`) VALUES
(1, 'Mary', 'password1'),
(2, 'Bob', 'password2'),
(3, 'Alice', 'password3'),
(4, 'Chris', 'password4'),
(5, 'Joe', 'password5');