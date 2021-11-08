# rachel.yong.2019 

import unittest
import flask_testing
from lesson import Lesson, db, app

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestLesson(TestApp):
    def test_lesson_creation(self):
        lesson1 = Lesson(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            description = 'Learn about Ink Qualities'
        )

        create_lesson_url = "/lesson/" + lesson1.course_name + "/" + str(lesson1.class_id) + "/" + str(lesson1.lesson_id)

        response = self.client.post(create_lesson_url)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, 
            {
                "code": 201,
                "data": {
                    "new_lesson": {
                        "course_name": 'Ink Course',
                        "class_id": 1,
                        "lesson_id": 1,
                        "description": 'This is Lesson 1'
                    }
                },
                "message": "Lesson commited to database."
            })

    def test_lesson_retrieval(self):
        lesson1 = Lesson(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            description = 'Learn about Ink Qualities'
        )

        lesson2 = Lesson(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 2,
            description = 'Learn about Ink Temperature'
        )

        db.session.add(lesson1)
        db.session.add(lesson2)
        db.session.commit()

        get_lesson_url = "/lesson/" + lesson1.course_name + "/" + str(lesson1.class_id)

        response = self.client.get(get_lesson_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 
            {
                "code": 200,
                "data": {
                    "lesson": [
                        {
                            "course_name": 'Ink Course',
                            "class_id": 1,
                            "lesson_id": 1,
                            "description": 'Learn about Ink Qualities'
                        },
                        {
                            "course_name": 'Ink Course',
                            "class_id": 1,
                            "lesson_id": 2,
                            "description": 'Learn about Ink Temperature'
                        },
                    ]
                }
            })

if __name__ == "__main__":
    unittest.main()