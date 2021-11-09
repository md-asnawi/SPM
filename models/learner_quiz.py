from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from learner import Learner
from quiz import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:WxJJy9gTnsC9@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Quiz(db.Model):

    __tablename__ = 'learner_quiz'
    __mapper_args__ = {'polymorphic_identity': 'learner_quiz'}

    course_name = db.Column(db.String(45), db.ForeignKey(Quiz.course_name), primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Quiz.class_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Quiz.lesson_id), primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.quiz_id), primary_key = True)
    learner_id = db.Column(db.Integer, db.ForeignKey(Learner.learner_id), primary_key = True)
    score = db.Column(db.Integer, nullable=False)
    passboolean = db.Column(db.Boolean, nullable=False)

    def __init__(self, course_name, class_id, lesson_id, quiz_id, learner_id, score, passboolean):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.quiz_id = quiz_id
        self.learner_id = learner_id
        self.score = score
        self.passboolean = passboolean

    def json(self):
        return {
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id, "quiz_id": self.quiz_id, "learner_id": self.learner_id, "score": self.score, "passboolean": self.passboolean
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

    def get_passboolean(self):
        return self.passboolean

    def set_score(self, passboolean):
        self.passboolean = passboolean

@app.route("/quizscore/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:quiz_id>/<int:learner_id>", methods=["GET"])
def get_quiz_score(course_name, class_id, lesson_id, quiz_id, learner_id):
    quiz_score = Learner_Quiz.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id, quiz_id = quiz_id, learner_id = learner_id).first()

    if quiz_score:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz_score": quiz_score.json()
                }
            }
        )

    return jsonify(
        {
            "message": "No quiz score found."
        }
    ), 500


@app.route("/quizscore/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:quiz_id>/<int:learner_id>/<int:score>", methods=["POST"])
def create_quiz_score(course_name, class_id, lesson_id, quiz_id, learner_id, score):

    if (score >= 85):
        new_quiz_score = Learner_Quiz(course_name, class_id, lesson_id, quiz_id, learner_id, score, True)
    else:
        new_quiz_score = Learner_Quiz(course_name, class_id, lesson_id, quiz_id, learner_id, score, False)

    
    try:
        db.session.add(new_quiz_score)
        db.session.commit()
        
        return jsonify (
            {
                "code": 201,
                "data": {
                    "new_quiz_score": new_quiz_score.json()
                },
                "message": "Quiz score commited to database."
            }
        ), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database.",
            "error": e
        }), 500

@app.route("/quizscore/update/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:quiz_id>/<int:learner_id>/<int:score>", methods=["PUT"])
def update_quiz_score(course_name, class_id, lesson_id, quiz_id, learner_id, score):

    quiz_score = Learner_Quiz.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id, quiz_id = quiz_id, learner_id = learner_id).first()

    if quiz_score:
        quiz_score.score = score
        if score >= 85:
            quiz_score.passboolean = True
        else:
            quiz_score.passboolean  = False

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz_score": quiz_score.json()
                }
            }
        )
    
    return jsonify(
            {
                "message": "Failed to update score"
            }
        ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)