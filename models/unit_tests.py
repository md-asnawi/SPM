import unittest
import datetime

from course import Course
# from Class import Class
# from lesson import Lesson
# from material import Material
# testing jenkin
# Test for class Course
class TestCourse(unittest.TestCase):
    def test_to_json(self):
        course1 = Course('Course 111', 111, 'This is Course 111',
                         '', datetime.date(2021, 1, 1), datetime.date(2021, 5, 1))
        self.assertEqual(course1.json(), {
            'course_name': 'Course 111',
            'course_id': 111,
            'description': 'This is Course 111',
            'prerequisite': '',
            'enrolment_start_date': '2021-01-01',
            'enrolment_end_date': '2021-05-01'
            }
        )
# # Test for class Class
# class TestClass(unittest.TestCase):
#     def test_to_json(self):
#         class1 = Class('Course 111', 1, 40, datetime.date(2021, 1, 1),
#                         datetime.date(2021, 4, 1), datetime.time(8, 15),
#                         datetime.time(11, 30), 'Deez')
#         self.assertEqual(class1.json(), {
#                 'course_name': 'Course 111',
#                 'class_id': 1,
#                 'class_size': 40,
#                 'start_date': '2021-01-01',
#                 'end_date': '2021-04-01',
#                 'start_time': '08:15:00',
#                 'end_time': '11:30:00',
#                 'trainer_name': 'Deez'
#             }
#         )

# # Test for class Lesson
# class TestLesson(unittest.TestCase):
#     def test_to_json(self):
#         lesson1 = Lesson('Course 111', 1, 1, True, 75)
#         self.assertEqual(lesson1.json(), {
#                 'course_name': 'Course 111',
#                 'class_id': 1,
#                 'lesson_id': 1,
#                 'ungraded_quiz': True,
#                 'completion_status': 75
#             }
#         )

# # Test for class Material
# class TestMaterial(unittest.TestCase):
#     def test_to_json(self):
#         material1 = Material(1, 'Material 1', '', 'Quiz', 100001, 'Course 111', 1, 1)
#         self.assertEqual(material1.json(), {
#                 'material_id': 1,
#                 'material_name': 'Material 1',
#                 'format': '',
#                 'material_type': 'Quiz',
#                 'uploader': 100001,
#                 'course_name': 'Course 111',
#                 'class_id': 1,
#                 'lesson_id': 1
#             }
#         )

if __name__ == "__main__":
    unittest.main()