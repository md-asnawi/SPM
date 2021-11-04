  CREATE DATABASE IF NOT EXISTS `is212`;
  USE `is212`;

  DROP TABLE IF EXISTS `course`;

  CREATE TABLE IF NOT EXISTS `course` (
    `course_id` INT NOT NULL,
    `course_name` VARCHAR(45) NOT NULL,
    `description` VARCHAR(45) NOT NULL,
    `prerequisite` VARCHAR(45) NULL,
    PRIMARY KEY (`course_name`),
    FOREIGN KEY (`prerequisite`) REFERENCES `course`(`course_name`)
  );

  INSERT INTO `course` (`course_id`, `course_name`, `description`, `prerequisite`) VALUES
  (111, 'Ink Course', 'You will learn about ink', NULL),
  (222, 'Data Course', 'You will learn about data', NULL),
  (333, 'Printer Course', 'You will learn about printer', 'Ink Course'),
  (444, 'Design Course', 'You will learn about design', 'Printer Course'),
  (555, 'Drawing Course', 'You will learn about drawing', NULL);