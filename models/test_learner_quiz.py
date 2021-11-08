#ID: kelionelmak.2019
#Matric Number: 01350993

import unittest
import flask_testing
from learner_quiz import Learner_Quiz, db as db1, app
from learner import Learner, db as db2
from quiz import Quiz, db as db3
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


class TestLearnerQuiz(TestApp):
    def test_learner_quiz_creation(self):
        quiz1 = Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            quiz_type = 'Ungraded'

        )

        learner1 = Learner(
            engineer_name = 'Nawi',
            engineer_id = 1,
            learner_id = 1
        )

        learner_quiz_1 = Learner_Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            learner_id = 1,
            score = 33,
            passboolean = False
        )

        db3.session.add(quiz1)
        db2.session.add(learner1)
        # db1.session.add(learner_quiz_1)
        # db1.session.commit()
        db2.session.commit()
        db3.session.commit()


        create_learner_quiz_url = "/quizscore/" + learner_quiz_1.course_name + "/" + str(learner_quiz_1.class_id) + "/" + str(learner_quiz_1.lesson_id)  + "/" +  str(learner_quiz_1.learner_id) + "/" + str(learner_quiz_1.quiz_id) + "/" + str(learner_quiz_1.score)

        response = self.client.post(create_learner_quiz_url)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json,
            {
                "code": 201,
                "data": {
                    "new_quiz_score": {
                        "course_name": "Ink Course",
                        "class_id": 1,
                        "lesson_id": 1,
                        "quiz_id": 1,
                        "learner_id": 1,
                        "score": 33,
                        "passboolean": False
                    }
                },
                "message": "Quiz score commited to database."
            })

    def test_learner_quiz_update(self):
        quiz1 = Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            quiz_type = 'Ungraded'

        )

        learner1 = Learner(
            engineer_name = 'Nawi',
            engineer_id = 1,
            learner_id = 1
        )

        learner_quiz_1 = Learner_Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            learner_id = 1,
            score = 33,
            passboolean = False
        )

        db3.session.add(quiz1)
        db2.session.add(learner1)
        db1.session.add(learner_quiz_1)
        db1.session.commit()
        db2.session.commit()
        db3.session.commit()

        updated_score = 100

        update_learner_quiz_url = "/quizscore/update/" + learner_quiz_1.course_name + "/" + str(learner_quiz_1.class_id) + "/" + str(learner_quiz_1.lesson_id) + "/" + str(learner_quiz_1.quiz_id) + "/" +  str(learner_quiz_1.learner_id) + "/" + str(updated_score)

        response = self.client.put(update_learner_quiz_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,
            {
                "code": 200,
                "data": {
                    "quiz_score": {
                        "course_name": "Ink Course",
                        "class_id": 1,
                        "lesson_id": 1,
                        "quiz_id": 1,
                        "learner_id": 1,
                        "score": 100,
                        "passboolean": True
                    }
                }
            })

if __name__ == "__main__":
    unittest.main()