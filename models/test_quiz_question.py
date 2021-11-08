# Led by Muhammad Asnawi (muhammadw.2019)

import unittest
import flask_testing
from quiz import Quiz, db as db1
from quiz_question import Quiz_Question, db as db2, app

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db1.create_all()
        db2.create_all()

    def tearDown(self):
        db1.session.remove()
        db1.drop_all()
        db2.session.remove()
        db2.drop_all()


class TestQuizQuestion(TestApp):
    def test_quiz_question_creation(self):
        quiz1 = Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            quiz_type = 'Ungraded'
        )

        db1.session.add(quiz1)
        db1.session.commit()

        quiz_question_1 = Quiz_Question(
            course_name = "Ink Course",
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            question_number = 1,
            question = 'True or False',
            question_type = 'TF',
            option_1 = 'True',
            option_2 = 'False',
            option_3 = 'null',
            option_4 = 'null',
            answer = 'True'
        )

        create_quiz_question_url = "/quizquestion/" + quiz_question_1.course_name + "/" + str(quiz_question_1.class_id) + "/" + str(quiz_question_1.lesson_id) + "/" + str(quiz_question_1.quiz_id) + "/" + str(quiz_question_1.question_number) + "/" + quiz_question_1.question + "/" + quiz_question_1.question_type + "/" + quiz_question_1.option_1 + "/" + quiz_question_1.option_2 + "/" + quiz_question_1.option_3 + "/" + quiz_question_1.option_4 + "/" + quiz_question_1.answer

        response = self.client.post(create_quiz_question_url)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, 
            {
                "code": 201,
                "data": {
                    "new_quiz_question": {
                        "course_name": "Ink Course",
                        "class_id": 1,
                        "lesson_id": 1,
                        "quiz_id": 1,
                        "question_number": 1,
                        "question": 'True or False',
                        "question_type": 'TF',
                        "option_1":'True',
                        "option_2": 'False',
                        "option_3": 'null',
                        "option_4": 'null',
                        "answer": 'True'
                    }
                },
                "message": "New Quiz Question commited to database."
            })

    def test_quiz_question_retrieval(self):
        quiz1 = Quiz(
            course_name = 'Ink Course',
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            quiz_type = 'Ungraded'
        )

        quiz_question_1 = Quiz_Question(
            course_name = "Ink Course",
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            question_number = 1,
            question = 'True or False',
            question_type = 'TF',
            option_1 = 'True',
            option_2 = 'False',
            option_3 = 'null',
            option_4 = 'null',
            answer = 'True'
        )

        quiz_question_2 = Quiz_Question(
            course_name = "Ink Course",
            class_id = 1,
            lesson_id = 1,
            quiz_id = 1,
            question_number = 2,
            question = 'Blue or Red or Green or Yellow',
            question_type = 'MCQ',
            option_1 = 'Blue',
            option_2 = 'Red',
            option_3 = 'Green',
            option_4 = 'Yellow',
            answer = 'Yellow'
        )

        db1.session.add(quiz1)
        db1.session.add(quiz_question_1)
        db1.session.add(quiz_question_2)
        db1.session.commit()        

        get_quiz_question_url = "/quiz/question/" + quiz1.course_name + "/" + str(quiz1.class_id) + "/" + str(quiz1.lesson_id) + "/" + str(quiz1.quiz_id)

        response = self.client.get(get_quiz_question_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 
            {
                "code": 200,
                "data": {
                    "quiz_questions": [
                        {
                            "course_name": "Ink Course",
                            "class_id": 1,
                            "lesson_id": 1,
                            "quiz_id": 1,
                            "question_number": 1,
                            "question": 'True or False',
                            "question_type": 'TF',
                            "option_1":'True',
                            "option_2": 'False',
                            "option_3": 'null',
                            "option_4": 'null',
                            "answer": 'True'
                        },
                        {
                            "course_name": "Ink Course",
                            "class_id": 1,
                            "lesson_id": 1,
                            "quiz_id": 1,
                            "question_number": 2,
                            "question": 'Blue or Red or Green or Yellow',
                            "question_type": 'MCQ',
                            "option_1":'Blue',
                            "option_2": 'Red',
                            "option_3": 'Green',
                            "option_4": 'Yellow',
                            "answer": 'Yellow'
                        }
                    ]
                }
            })

if __name__ == "__main__":
    unittest.main()