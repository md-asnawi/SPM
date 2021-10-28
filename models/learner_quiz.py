from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from learner import Learner
from quiz import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Quiz(db.Model):

    course_name = db.Column(db.String(45), db.ForeignKey(Quiz.course_name), primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Quiz.class_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Quiz.lesson_id), primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.quiz_id), primary_key = True)
    learner_id = db.Column(db.Integer, db.ForeignKey(Learner.learner_id), primary_key = True)
    score = db.Column(db.Integer, nullable=True)

    def __init__(self, course_name, class_id, lesson_id, quiz_id, learner_id, score):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.quiz_id = quiz_id
        self.learner_id = learner_id
        self.score = score

    def json(self):
        return {
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id, "quiz_id": self.quiz_id, "learner_id": self.learner_id, "score": self.score
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

    def get_learner_id(self):
        return self.learner_id

    def set_leaner_id(self, learner_id):
        self.learner_id = learner_id

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)