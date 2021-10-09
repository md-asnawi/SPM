# Course
# class_list is an attribute which contains all the Class objects
# e.g. Course SPM will have attribute class_list, which contains Class G1, Class G2...
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

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
                "enrolment_start_date": self.enrolment_start_date, "enrolment_end_date": self.enrolment_end_date}

    def get_course_name(self):
        return self.course_name
    
    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_course_id(self):
        return self.course_id

    def set_course_id(self, course_id):
        self.course_id = course_id

    def get_class_list(self):
        return self.class_list

    def add_class(self, Class):
        self.class_list.append(Class)

    def remove_class(self, Class):
        self.class_list.remove(Class)

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

# @app.route("/course/<eid:engineer_id>", methods=["GET"])
# def get_available(engineer_id):
#     courselist = Course.query.all() 
#     engineer_course_completed = Engineer.query.filter_by(engineer_id=engineer_id).all()

#     ## if course_completed, should remove from courselist..
#     for course in courselist:
#         for course_completed in engineer_course_completed:
#             if course == course_completed:
#                 courselist.remove(course)

#     if len(courselist):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "course": [course.json() for course in engineer_course_completed]
#                 }
#             }
#         )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)