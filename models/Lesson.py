# Lesson, part of Class

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Lesson(db.Model):

    course_name = db.Column(db.String(45), primary_key = True)
    class_id = db.Column(db.Integer, primary_key = True)
    lesson_id = db.Column(db.Integer, primary_key = True)
    ungraded_quiz = db.Column(db.Boolean, nullable = False)
    completion_status = db.Column(db.Integer, nullable = False)

    def __init__(self, course_name, class_id, lesson_id, ungraded_quiz, completion_status):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.ungraded_quiz = ungraded_quiz
        self.completion_status = completion_status

    def json(self):
        return {
                "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id, 
                "ungraded_quiz": self.ungraded_quiz, "completion_status": self.completion_status
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

    def get_ungraded_quiz(self):
        return self.ungraded_quiz

    def set_ungraded_quiz(self, ungraded_quiz):
        self.ungraded_quiz = ungraded_quiz

    def get_completion_status(self):
        return self.completion_status

    def set_completion_status(self, completion_status):
        self.completion_status = completion_status


# GET all lessons with course name & class id
@app.route("/lesson/<string:course_name>/<int:class_id>", methods=["GET"])
def get_all_lessons_by_class(course_name, class_id):

    lessonList = Lesson.query.filter_by(course_name = course_name, class_id = class_id).all()  
    
    if len(lessonList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lesson": [lesson.json() for lesson in lessonList]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "No lessons found. Check course name or class id."
        }
    )

# GET 1 lesson with course name, class id, lesson id
@app.route("/lesson/<string:course_name>/<int:class_id>/<int:lesson_id>", methods=["GET"])
def get_lesson(course_name, class_id, lesson_id):

    lesson = Lesson.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id).first()  
    
    if lesson:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lesson": lesson.json()
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Lesson not found. Check course name, class id or lesson id."
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    