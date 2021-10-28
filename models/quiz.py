from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from lesson import Lesson

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Quiz(db.Model):

    __tablename__ = 'quiz'
    __mapper_args__ = {'polymorphic_identity': 'quiz'}

    course_name = db.Column(db.String(45), db.ForeignKey(Lesson.course_name), primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Lesson.class_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Lesson.class_id), primary_key = True)
    quiz_id = db.Column(db.Integer, primary_key = True)
    quiz_type = db.Column(db.String(45), nullable = False)

    def __init__(self, course_name, class_id, lesson_id, quiz_id, quiz_type):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.quiz_id = quiz_id
        self.quiz_type = quiz_type

    def json(self):
        return {
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id, "quiz_id": self.quiz_id, "quiz_type": self.quiz_type
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)