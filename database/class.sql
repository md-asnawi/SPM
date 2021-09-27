CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `class`;

CREATE TABLE IF NOT EXISTS `class` (
  `class_id` INT NOT NULL,
  `class_name` VARCHAR(45) NULL,
  PRIMARY KEY (`class_id`)
);

INSERT INTO `class` (`class_id`, `class_name`) VALUES
('1', 'Class 1'),
('2', 'Class 2'),
('3', 'Class 3'),
('4', 'Class 4'),
('5', 'Class 5');