from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from quiz import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Quiz_Question(db.Model):

    __tablename__ = 'quiz_question'
    __mapper_args__ = {'polymorphic_identity': 'quiz_question'}

    course_name = db.Column(db.String(45), db.ForeignKey(Quiz.course_name), primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Quiz.class_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Quiz.lesson_id), primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.quiz_id), primary_key = True)
    quiz_type = db.Column(db.String(45), nullable = False)
    question_number = db.Column(db.Integer, primary_key = True)
    question  = db.Column(db.String(255), nullable = False)
    question_type  = db.Column(db.String(45), nullable = False)
    option_1 = db.Column(db.String(45), nullable = False)
    option_2 = db.Column(db.String(45), nullable = False)
    option_3 = db.Column(db.String(45), nullable = True)
    option_4 = db.Column(db.String(45), nullable = True)
    answer = db.Column(db.String(45), nullable = False)
    

    def __init__(self, course_name, class_id, lesson_id, quiz_id, quiz_type, question_number, question, question_type, option_1, option_2, option_3, option_4, answer):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.quiz_id = quiz_id
        self.quiz_type = quiz_type
        self.question_number = question_number
        self.question = question
        self.question_type = question_type
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.answer = answer

    def json(self):
        return {
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id, "quiz_id": self.quiz_id, "quiz_type": self.quiz_type,
            "question_number": self.question_number, "question": self.question, "question_type": self.question_type, "option_1": self.option_1,
            "option_2": self.option_2, "option_3": self.option_3, "option_4": self.option_4, "answer": self.answer
        }

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id

    def get_lesson_id(self):
        return self.lesson_id

    def set_lesson_id(self, lesson_id):
        self.lesson_id = lesson_id

    def get_quiz_id(self):
        return self.quiz_id

    def set_quiz_id(self, quiz_id):
        self.quiz_id = quiz_id

    def get_quiz_type(self):
        return self.quiz_type

    def set_quiz_type(self, quiz_type):
        self.quiz_type = quiz_type

    def get_question_number(self):
        return self.question_number

    def set_question_number(self, question_number):
        self.question_number = question_number

    def get_question(self):
        return self.question

    def set_question(self, question):
        self.question = question

    def get_question_type(self):
        return self.question_type

    def set_question_type(self, question_type):
        self.question_type = question_type

    def get_option_1(self):
        return self.option_1

    def set_option_1(self, option_1):
        self.option_1 = option_1

    def get_option_2(self):
        return self.option_2

    def set_option_2(self, option_2):
        self.option_2 = option_2

    def get_option_3(self):
        return self.option_3

    def set_option_3(self, option_3):
        self.option_3 = option_3

    def get_option_4(self):
        return self.option_4

    def set_option_4(self, option_4):
        self.option_4 = option_4

    def get_answer(self):
        return self.answer

    def set_answer(self, answer):
        self.answer = answer


@app.route("/quiz/question/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:quiz_id>", methods=["GET"])
def get_quiz_questions(course_name, class_id, lesson_id, quiz_id):

    quiz_questions_list = Quiz_Question.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id, quiz_id = quiz_id).all()
    
    if len(quiz_questions_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz_questions": [quiz_question.json() for quiz_question in quiz_questions_list]
                }
            }
        )

    return jsonify(
        {
            "message": "No quiz found."
        }
    ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)