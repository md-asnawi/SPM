#TDD by jocastaheng.2019

import unittest
import flask_testing
from course import Course, db, app

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


class TestCourse(TestApp):
    def test_course_creation(self):
        course1 = Course(
            course_id = 111,
            course_name = 'Ink Course',
            description = 'This is Course 111',
            prerequisite = 'Data Course'
        )

        course_url = "/createcourse/" + str(course1.course_id) + "/"  + course1.course_name + "/" + course1.description + "/" + course1.prerequisite

        response = self.client.post(course_url)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, 
            {
                "code": 201,
                "data": {
                    "new_quiz_score": {
                        "course_id": 111,
                        "course_name": "Ink Course",
                        "description": "This is Course 111",
                        "prerequisite": 'Data Course'
                    }
                },
                "message": "Course commited to database."
            })

    def test_course_retrieval(self):
        course1 = Course(
            course_id = 111,
            course_name = 'Ink Course',
            description = 'This is Course 111',
            prerequisite = 'Data Course'
        )

        course2 = Course(
            course_id = 222,
            course_name = 'Data Course',
            description = 'This is Course 222',
            prerequisite = 'null'
        )

        db.session.add(course2)
        db.session.add(course1)
        db.session.commit()

        get_course_url = "/course"

        response = self.client.get(get_course_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 
            {
                "code": 200,
                "data": {
                    "course": [
                        {
                            "course_id": 111,
                            "course_name": 'Ink Course',
                            "description": 'This is Course 111',
                            "prerequisite": 'Data Course'
                        },
                        {
                            "course_id": 222,
                            "course_name": 'Data Course',
                            "description": 'This is Course 222',
                            "prerequisite": 'null'
                        }
                    ]
                }
            })

if __name__ == "__main__":
    unittest.main()