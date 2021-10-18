CREATE DATABASE IF NOT EXISTS `is212`;
USE `is212`;

DROP TABLE IF EXISTS `class`;

CREATE TABLE IF NOT EXISTS `class` (
  `course_name` VARCHAR(45) NOT NULL,
  `class_id` INT NOT NULL,
  `class_size` VARCHAR(45) NOT NULL,
  `start_date` DATE NOT NULL, 
  `end_date` DATE NOT NULL, 
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `trainer_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`course_name`, `class_id`),
  FOREIGN KEY (`course_name`) REFERENCES `course`(`course_name`)
);

INSERT INTO `class` (`course_name`, `class_id`, `class_size`, `start_date`, `end_date`, `start_time`, `end_time`, `trainer_name`) VALUES
('Course 111', '1', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Mong'),
('Course 111', '2', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Dong'),
('Course 222', '1', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Kook'),
('Course 333', '1', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Jong'),
('Course 444', '1', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Soo'),
('Course 555', '1', '40', '2021-04-01', '2021-10-01', '08:15:00', '12:00:00', 'Woo');