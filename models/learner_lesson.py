from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from lesson import Lesson
from learner_class import Learner_Class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:WxJJy9gTnsC9@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Lesson(db.Model):

    __tablename__ = 'learner_lesson'
    __mapper_args__ = {'polymorphic_identity': 'learner_lesson'}

    course_name = db.Column(db.String(45), db.ForeignKey(Lesson.course_name), primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Lesson.class_id), primary_key = True)
    learner_id = db.Column(db.Integer, db.ForeignKey(Learner_Class.learner_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Lesson.lesson_id), primary_key = True)
    is_completed = db.Column(db.Boolean, nullable = False)

    def __init__(self, course_name, class_id, lesson_id, learner_id, is_completed):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.learner_id = learner_id
        self.is_completed = is_completed

    def json(self):
        return {
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id,
            "learner_id": self.learner_id, "is_completed": self.is_completed
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

    def get_learner_id(self):
        return self.learner_id

    def set_learner_id(self, learner_id):
        self.learner_id = learner_id

    def get_is_completed(self):
        return self.is_completed

    def set_is_completed(self, is_completed):
        self.is_completed = is_completed


# get all lessons of learner for a course
# use course name because learners can only attend 1 class in the course
# cannot use class id because learners classes in different course can have same class id
@app.route("/learner_lesson/<string:course_name>/<int:learner_id>", methods=["GET"])
def get_lessons_by_course_name_and_learner_id(course_name, learner_id):

    learner_lessons = Learner_Lesson.query.filter_by(course_name = course_name,learner_id = learner_id).all()
    
    if len(learner_lessons):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_lesson": [learner_lesson.json() for learner_lesson in learner_lessons]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Learner lesson not found."
        }
    ), 404

# get 1 learner_lesson record using the course_name, learner_id and lesson_id
@app.route("/learner_lesson/<string:course_name>/<int:learner_id>/<int:lesson_id>", methods=["GET"])
def get_lessons_by_course_name_and_learner_id_and_lesson_id(course_name, learner_id, lesson_id):

    learner_lesson = Learner_Lesson.query.filter_by(course_name = course_name,learner_id = learner_id, lesson_id=lesson_id).first()
    
    if learner_lesson:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_lesson": learner_lesson.json()
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Learner lesson not found."
        }
    ), 404


# get all learner_lesson records of completed lessons for a learner using the course_name, learner_id
@app.route("/learner_lesson/completed/<string:course_name>/<int:learner_id>", methods=["GET"])
def get_completed_lessons(course_name, learner_id):

    learner_lessons = Learner_Lesson.query.filter_by(course_name = course_name,learner_id = learner_id, is_completed = 1).all()
    
    if len(learner_lessons):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_lesson": [learner_lesson.json() for learner_lesson in learner_lessons]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Learner lesson not found."
        }
    ), 404


# update the completion status of a lesson using course name, learner id, lesson id
@app.route("/learner_lesson/update_completion/<string:course_name>/<int:learner_id>/<int:lesson_id>", methods=["PUT"])
def update_completion_status(course_name, learner_id, lesson_id):

    learner_lesson = Learner_Lesson.query.filter_by(course_name = course_name,learner_id = learner_id, lesson_id=lesson_id).first()
    
    if learner_lesson:
        learner_lesson.is_completed = True
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_lesson": learner_lesson.json()
                }
            }
        )

    return jsonify(
            {
                "code": 404,
                "data": {
                    "course_name": course_name,
                    "learner_id": learner_id,
                    "lesson_id": lesson_id
                },
                "message": "Learner or Class not found"
            }
        ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5013, debug=True)