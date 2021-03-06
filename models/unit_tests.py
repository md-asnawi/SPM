import unittest
import datetime

from course import Course
from Class import Class
from lesson import Lesson
from material import Material
from quiz import Quiz

# Test for class Course
class TestCourse(unittest.TestCase):
    def test_to_json(self):
        course1 = Course('Course 111', 111, 'This is Course 111', '')
        self.assertEqual(course1.json(), {
            'course_name': 'Course 111',
            'course_id': 111,
            'description': 'This is Course 111',
            'prerequisite': ''
            }
        )
# Test for class Class
class TestClass(unittest.TestCase):
    def test_to_json(self):
        class1 = Class('Course 111', 1, 40, datetime.date(2021, 1, 1),
                        datetime.date(2021, 4, 1), datetime.date(2021, 1, 1),
                        datetime.date(2021, 4, 1), datetime.time(8, 15),
                        datetime.time(11, 30), 'Deez')

        self.assertEqual(class1.json(), {
                'course_name': 'Course 111',
                'class_id': 1,
                'class_size': 40,
                'enrolment_start_date': '2021-01-01',
                'enrolment_end_date': '2021-04-01',
                'class_start_date': '2021-01-01',
                'class_end_date': '2021-04-01',
                'start_time': '08:15:00',
                'end_time': '11:30:00',
                'trainer_name': 'Deez'
            }
        )

# Test for class Lesson
class TestLesson(unittest.TestCase):
    def test_to_json(self):
        lesson1 = Lesson('Course 111', 1, 1, "This is Course 111")
        self.assertEqual(lesson1.json(), {
                'course_name': 'Course 111',
                'class_id': 1,
                'lesson_id': 1,
                "description": "This is Course 111"
            }
        )

# Test for class Material
class TestMaterial(unittest.TestCase):
    def test_to_json(self):
        material1 = Material(1, 'Material 1', '', 'Quiz', 100001, 'Course 111', 1, 1)
        self.assertEqual(material1.json(), {
                'material_id': 1,
                'material_name': 'Material 1',
                'format': '',
                'material_type': 'Quiz',
                'uploader': 100001,
                'course_name': 'Course 111',
                'class_id': 1,
                'lesson_id': 1
            }
        )

class TestQuiz(unittest.TestCase):
    def test_to_json(self):
        quiz1 = Quiz('Course 111', 1, 1, 1, "Ungraded")
        self.assertEqual(quiz1.json(), {
                'course_name': 'Course 111',
                'class_id': 1,
                'lesson_id': 1,
                'quiz_id': 1,
                'quiz_type': 'Ungraded'
            }
        )

if __name__ == "__main__":
    unittest.main()