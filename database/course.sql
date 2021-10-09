CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `course`;

CREATE TABLE IF NOT EXISTS `course` (
  `course_id` INT NOT NULL,
  `course_name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(45) NOT NULL,
  `prerequisite` VARCHAR(45) NULL,
  `enrolment_start_date` DATE NOT NULL,
  `enrolment_end_date` DATE NOT NULL,
  PRIMARY KEY (`course_name`),
  FOREIGN KEY (`prerequisite`) REFERENCES `course`(`course_name`)
);

INSERT INTO `course` (`course_id`, `course_name`, `description`, `prerequisite`, `enrolment_start_date`, `enrolment_end_date`) VALUES
('111', 'Course 111', 'This is Course 111', NULL, '2021-01-01', '2021-04-01'),
('222', 'Course 222', 'This is Course 222', NULL, '2021-01-01', '2021-04-01'),
('333', 'Course 333', 'This is Course 333', 'Course 111', '2021-01-01', '2021-04-01'),
('444', 'Course 444', 'This is Course 444', 'Course 333', '2021-01-01', '2021-04-01'),
('555', 'Course 555', 'This is Course 555', NULL, '2021-01-01', '2021-04-01');