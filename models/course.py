# Course
# class_list is an attribute which contains all the Class objects
# e.g. Course SPM will have attribute class_list, which contains Class G1, Class G2...
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from learner_class import Learner_Class

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Course(db.Model):

    __tablename__ = 'course'

    course_name = db.Column(db.String(45), nullable=False)
    course_id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(45), nullable=False)
    prerequisite = db.Column(db.Integer, nullable=False)
    enrolment_start_date = db.Column(db.Date, nullable=False)
    enrolment_end_date = db.Column(db.Date, nullable=False)

    def __init__(self, course_name = "", course_id = "", description = "", prerequisite = "", enrolment_start_date = "", enrolment_end_date = ""):
        self.course_name = course_name
        self.course_id = course_id
        self.description = description
        self.prerequisite = prerequisite
        self.enrolment_start_date = enrolment_start_date
        self.enrolment_end_date = enrolment_end_date

    def json(self):
        return{"course_name": self.course_name, "course_id": self.course_id, "description": self.description, "prerequisite": self.prerequisite,
                "enrolment_start_date": str(self.enrolment_start_date), "enrolment_end_date": str(self.enrolment_end_date)}

    def get_course_name(self):
        return self.course_name
    
    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_course_id(self):
        return self.course_id

    def set_course_id(self, course_id):
        self.course_id = course_id

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_prerequisite(self):
        return self.prerequisite

    def set_prerequisite(self, prerequisite):
        self.prerequisite = prerequisite

    def get_enrolment_start_date(self):
        return self.enrolment_start_date

    def set_enrolment_start_date(self, enrolment_start_date):
        self.enrolment_start_date = enrolment_start_date

    def get_enrolment_end_date(self):
        return self.enrolment_end_date

    def set_enrolment_end_date(self, enrolment_end_date):
        self.enrolment_end_date = enrolment_end_date
    
# all course
@app.route("/course", methods=["GET"])
def get_all():

    courselist = Course.query.all()
    
    if len(courselist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in courselist]
                }
            }
        )

# course count
@app.route("/course/count", methods=["GET"])
def get_course_count():

    courselist = Course.query.all()
    
    if len(courselist):
        count = 0
        for course in courselist:
            count += 1

        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_count": count
                }
            }
        )

@app.route("/course/available/<int:learner_id>", methods=["GET"])
def get_available(learner_id):

    unavailable_array = []
    available_course = []

    courselist = Course.query.all()

    # get learner course completed
    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id).all()

    for eachrow in learner_class:
        # if in the learner_class and not withdrawn, means unavailable
        if eachrow.json()["withdrawal"] == False:
            unavailable_array.append(eachrow.json()["course_name"])
    
    # if course not in completed array, append to available array.
    if len(courselist):
        for course in courselist:
            if course.json()["course_name"] not in unavailable_array:
                available_course.append(course)
                
    # display available array    
    if len(available_course):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in available_course]
                }
            }
        )

    else:
        return jsonify({
            "code": 404,
            "message": "No Available Course"
        }), 404

@app.route("/course/completed/<int:learner_id>", methods=["GET"])
def get_completed(learner_id):

    completed_array = []
    completed_course = []
    courselist = Course.query.all()

    # get learner course completed
    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id).all()

    for eachrow in learner_class:
        # if in the learner_class and progress 100, means completed
        if eachrow.json()["progress"] == 100:
            completed_array.append(eachrow.json()["course_name"])

    # if course completed, append to completed array.
    if len(courselist):
        for course in courselist:
            if course.json()["course_name"] in completed_array:
                completed_course.append(course)
                
    # display available array    
    if len(completed_course):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in completed_course]
                }
            }
        )
    else:
        return jsonify({
            "code": 404,
            "message": "No Course Completed"
        }), 404

@app.route("/course/enrolled/<int:learner_id>", methods=["GET"])
def get_enrolled(learner_id):

    enrolled_array = []
    enrolled_course = []
    courselist = Course.query.all()

    # get learner course enrolled
    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, enrolment_status="Enrolled", withdrawal=0).all()

    for eachrow in learner_class:
        # if in the learner_class and progress 100, means completed
        if eachrow.json()["progress"] != 100:
            enrolled_array.append(eachrow.json()["course_name"])

    # if course completed, append to completed array.
    if len(courselist):
        for course in courselist:
            if course.json()["course_name"] in enrolled_array:
                enrolled_course.append(course)
                
    # display available array    
    if len(enrolled_course):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in enrolled_course]
                }
            }
        )
    else:
        return jsonify({
            "code": 404,
            "message": "No Course Enrolled"
        }), 404
    
@app.route("/course/<string:course_name>", methods=["GET"])
def get_course_information(course_name):

    course = Course.query.filter_by(course_name=course_name).first()
    
    if course:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": course.json()
                }
            })
        
    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "course": "Course not found"
                }
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
