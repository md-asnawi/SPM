CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `class`;

CREATE TABLE IF NOT EXISTS `class` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `class_size` VARCHAR(45) NOT NULL,
  `enrolment_start_date` DATE NOT NULL,
  `enrolment_end_date` DATE NOT NULL,
  `class_start_date` DATE NOT NULL, 
  `class_end_date` DATE NOT NULL, 
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `trainer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`course_name`, `class_id`),
  FOREIGN KEY (`course_name`) REFERENCES `course`(`course_name`)
);

INSERT INTO `class` (`course_name`, `class_id`, `class_size`, `enrolment_start_date`, `enrolment_end_date`, `class_start_date`, `class_end_date`, `start_time`, `end_time`, `trainer_name`) VALUES
('Ink Course', 1, '40', '2021-01-01', '2021-02-01', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Mong'),
('Ink Course', 2, '40', '2021-02-01', '2021-03-01', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Dong'),
('Data Course', 1, '40', '2021-12-01', '2022-02-01', '2022-04-01', '2022-10-01', '08:15:00', '12:00:00', 'Kook'),
('Printer Course', 1, '40', '2021-02-01', '2021-03-01', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Jong'),
('Design Course', 1, '40', '2021-01-01', '2022-03-02', '2022-04-01', '2022-10-01', '08:15:00', '12:00:00', 'Soo'),
('Drawing Course', 1, '40', '2021-01-01', '2021-02-01', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Woo');
