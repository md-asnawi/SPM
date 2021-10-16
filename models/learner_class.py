# Learner & Class enrolment class

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Class(db.Model):

    __tablename__ = 'learner_class'

    course_name = db.Column(db.String(45), nullable=False, primary_key = True)
    class_id = db.Column(db.Integer, primary_key = True)
    learner_id = db.Column(db.Integer, nullable=False, primary_key = True)
    date_assigned = db.Column(db.Date, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    progress = db.Column(db.Integer, nullable=False)
    enrolment_status = db.Column(db.String(45), nullable=False)
    preassigned = db.Column(db.Boolean, nullable=False)
    withdrawal = db.Column(db.Boolean, nullable=False)

    def __init__(self, course_name = "", class_id = "", learner_id = "", date_assigned = "", start_date = "", end_date = "", 
                    progress = "", enrolment_status = "", preassigned = "", withdrawal = ""):
        self.course_name = course_name
        self.class_id = class_id
        self.learner_id = learner_id
        self.date_assigned = date_assigned
        self.start_date = start_date
        self.end_date = end_date
        self.progress = progress
        self.enrolment_status = enrolment_status
        self.preassigned = preassigned
        self.withdrawal = withdrawal

    def json(self):
        return{"course_name": self.course_name, "class_id": self.class_id, "learner_id": self.learner_id, "date_assigned": self.date_assigned,
                "start_date": self.start_date, "end_date": self.end_date, "progress": self.progress, "enrolment_status": self.enrolment_status, 
                "preassigned": self.preassigned, "withdrawal": self.withdrawal}

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id

    def get_learner_id(self):
        return self.learner_id

    def get_learner_id(self, learner_id):
        self.learner_id = learner_id

    def get_date_assigned(self):
        return self.date_assigned
    
    def set_date_assigned(self, date_assigned):
        self.date_assigned = date_assigned

    def get_start_date(self):
        return self.start_date
    
    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date
    
    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_progress(self):
        return self.progress
    
    def set_progress(self, progress):
        self.progress = progress

    def get_enrolment_status(self):
        return self.enrolment_status
    
    def set_enrolment_status(self, enrolment_status):
        self.enrolment_status = enrolment_status

    def get_preassigned(self):
        return self.preassigned
    
    def set_preassigned(self, preassigned):
        self.preassigned = preassigned

    def get_withdrawal(self):
        return self.withdrawal
    
    def set_withdrawal(self, withdrawal):
        self.withdrawal = withdrawal

# get pending count
@app.route("/pending/count", methods=["GET"])
def get_pending_count():

    learner_class_list = Learner_Class(db.Model).query.filter_by(enrolment_status="Pending").all()
    
    if len(learner_class_list):
        count = 0
        for learner in learner_class_list:
            count += 1

        return jsonify(
            {
                "code": 200,
                "data": {
                    "pending_count": count
                }
            }
        )

    else:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "pending_count": 0
                }
            }
        )

@app.route("/class/count/<string:course_name>/<int:class_id>", methods=["GET"])
def get_inclass_count(course_name, class_id):

    inclass_count = Learner_Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id,enrolment_status="Enrolled",withdrawal=0).all()

    if len(inclass_count):
        count = 0
        for learner in inclass_count:
            count += 1

        return jsonify(
            {
                "code": 200,
                "data": {
                    "inclass_count": count
                }
            }
        )

    else:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inclass_count": 0
                }
            }
        )

@app.route("/class/<string:course_name>", methods=["GET"])
def get_inclass(course_name):

    inclass = Learner_Class(db.Model).query.filter_by(course_name=course_name,enrolment_status="Enrolled",withdrawal=0).all()

    if len(inclass):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inclass": [course_class.json() for course_class in inclass]
                }
            }
        )

    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "inclass": "No one enrolled in this class."
                }
            }
        )

# whoever completed the course
@app.route("/course_completed/<string:course_name>", methods=["GET"])
def get_coursecompleted(course_name):

    learner_list = Learner_Class(db.Model).query.filter_by(course_name=course_name,enrolment_status="Enrolled",progress=100).all()

    if len(learner_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "completed_learner": [learner.json() for learner in learner_list]
                }
            }
        )

    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "completed_learner": "No one completed the course."
                }
            }
        )

# whoever completed the prereq
# @app.route("/course/prereq/<string:course_name>", methods=["GET"])
# def get_prereq(course_name):
#     course = Course(db.Model).query.filter_by(course_name=course_name).first()
#     course_prereq = course.prerequisite

#     prereq_learner_class = Learner_Class(db.Model).query.filter_by(course_name=course_prereq,enrolment_status="Enrolled",progress=100).all()

#     if len(prereq_learner_class):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "prereq_completed_learner": [learner.json() for learner in prereq_learner_class]
#                 }
#             }
#         )

#     else:
#         return jsonify(
#             {
#                 "code": 404,
#                 "data": {
#                     "prereq_completed_learner": "No one completed the prerequisite of this course."
#                 }
#             }
#         )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
    