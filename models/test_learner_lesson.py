# TDD by yichen.kwek.2019

import unittest
import flask_testing
from learner_lesson import Learner_Lesson, db as db1, app
from learner import Learner, db as db2
from lesson import Lesson, db as db3
from engineer import Engineer, db as db4

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db1.create_all()
        db2.create_all()
        db3.create_all()
        db4.create_all()


    def tearDown(self):
        db1.session.remove()
        db1.drop_all()
        db2.session.remove()
        db2.drop_all()
        db3.session.remove()
        db3.drop_all()
        db4.session.remove()
        db4.drop_all()


class TestLearnerLesson(TestApp):
    def test_learner_lesson_update(self):
        lesson1 = Lesson(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            description = 'Learn about Ink Qualities'
        )

        learner1 = Learner(
            engineer_name = 'Nawi',
            engineer_id = 1,
            learner_id = 1
        )

        learner_lesson_1 = Learner_Lesson(
            course_name = lesson1.course_name,
            class_id = lesson1.class_id,
            lesson_id = lesson1.lesson_id,
            learner_id = learner1.learner_id,
            is_completed = False
        )

        db3.session.add(lesson1)
        db2.session.add(learner1)
        db1.session.add(learner_lesson_1)
        db1.session.commit()
        db2.session.commit()
        db3.session.commit()


        learner_lesson_url = "/learner_lesson/update_completion/" + learner_lesson_1.course_name + "/" + str(learner_lesson_1.learner_id) + "/" + str(learner_lesson_1.lesson_id)

        response = self.client.put(learner_lesson_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 
            {
                "code": 200,
                "data": {
                    "learner_lesson": {
                        "course_name": 'Ink Course',
                        "class_id": 1,
                        "lesson_id": 1,
                        "learner_id": 1,
                        "is_completed": True
                    }
                }
            })

    def test_completed_learner_lesson_retrieval(self):
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

        lesson3 = Lesson(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 3,
            description = 'Learn about Ink Viscosity'
        )

        learner1 = Learner(
            engineer_name = 'Nawi',
            engineer_id = 1,
            learner_id = 1
        )

        learner_lesson_1 = Learner_Lesson(
            course_name = lesson1.course_name,
            class_id = lesson1.class_id,
            lesson_id = lesson1.lesson_id,
            learner_id = learner1.learner_id,
            is_completed = True
        )

        learner_lesson_2 = Learner_Lesson(
            course_name = lesson2.course_name,
            class_id = lesson2.class_id,
            lesson_id = lesson2.lesson_id,
            learner_id = learner1.learner_id,
            is_completed = True
        )

        learner_lesson_3 = Learner_Lesson(
            course_name = lesson3.course_name,
            class_id = lesson3.class_id,
            lesson_id = lesson3.lesson_id,
            learner_id = learner1.learner_id,
            is_completed = False
        )

        db3.session.add(lesson1)
        db3.session.add(lesson2)
        db3.session.add(lesson3)
        db2.session.add(learner1)
        db1.session.add(learner_lesson_1)
        db1.session.add(learner_lesson_2)
        db1.session.add(learner_lesson_3)
        db1.session.commit()
        db2.session.commit()
        db3.session.commit()

        get_learner_lesson_url = "/learner_lesson/completed/" + learner_lesson_1.course_name + "/" + str(learner_lesson_1.learner_id)

        response = self.client.get(get_learner_lesson_url)
        self.assertEqual(response.status_code, 200)

        # TO DO
        self.assertEqual(response.json, 
            {
                "code": 200,
                "data": {
                    "learner_lesson": [
                        {
                            "course_name": 'Ink Course',
                            "class_id": 1,
                            "lesson_id": 1,
                            "learner_id": 1,
                            "is_completed": True
                        },
                        {
                            "course_name": 'Ink Course',
                            "class_id": 1,
                            "lesson_id": 2,
                            "learner_id": 1,
                            "is_completed": True
                        }
                    ]
                }
            })
            

if __name__ == "__main__":
    unittest.main()