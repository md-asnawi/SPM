CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `course`;

CREATE TABLE IF NOT EXISTS `course` (
  `course_name` VARCHAR(45) NOT NULL,
  `course_id` INT NOT NULL,
  `description` VARCHAR(45) NOT NULL,
  `prerequisite` VARCHAR(45) NULL,
  PRIMARY KEY (`course_name`),
  FOREIGN KEY (`prerequisite`) REFERENCES `course`(`course_name`)
);

INSERT INTO `course` (`course_name`, `course_id`, `description`, `prerequisite`) VALUES
('Ink Course', 111, 'You will learn about ink', NULL),
('Data Course', 222, 'You will learn about data', NULL),
('Printer Course', 333, 'You will learn about printer', 'Ink Course'),
('Design Course', 444, 'You will learn about design', NULL),
('Drawing Course', 555, 'You will learn about drawing', NULL);