# Learner & Class enrolment class

from flask import Flask, request, jsonify
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
import sys

sys.path.append('./models')
from Class import Class


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:WxJJy9gTnsC9@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Class(db.Model):

    __tablename__ = 'learner_class'
    __mapper_args__ = {'polymorphic_identity': 'learner_class'}

    course_name = db.Column(db.String(45),db.ForeignKey(Class.course_name), nullable=False, primary_key = True)
    class_id = db.Column(db.Integer,db.ForeignKey(Class.class_id), primary_key = True)
    learner_id = db.Column(db.Integer, nullable=False, primary_key = True)
    date_assigned = db.Column(db.Date, nullable=False)
    progress = db.Column(db.Integer, nullable=False)
    enrolment_status = db.Column(db.String(45), nullable=False)
    preassigned = db.Column(db.Boolean, nullable=False)
    withdrawal = db.Column(db.Boolean, nullable=False)
    withdrawal_message = db.Column(db.String(255), nullable=True)


    def __init__(self, course_name = "", class_id = "", learner_id = "", date_assigned = "", 
                    progress = "", enrolment_status = "", preassigned = "", withdrawal = "", withdrawal_message = ""):
        self.course_name = course_name
        self.class_id = class_id
        self.learner_id = learner_id
        self.date_assigned = date_assigned
        self.progress = progress
        self.enrolment_status = enrolment_status
        self.preassigned = preassigned
        self.withdrawal = withdrawal
        self.withdrawal_message = withdrawal_message

    def json(self):
        return{"course_name": self.course_name, "class_id": self.class_id, "learner_id": self.learner_id, "date_assigned": self.date_assigned, 
                "progress": self.progress, "enrolment_status": self.enrolment_status, 
                "preassigned": self.preassigned, "withdrawal": self.withdrawal, "withdrawal_message": self.withdrawal_message}

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

    def get_withdrawal_message(self):
        return self.withdrawal_message
    
    def set_withdrawal_message(self, withdrawal_message):
        self.withdrawal_message = withdrawal_message

# get all courses learner enrolled in using learner id
@app.route("/learner_class/<int:learner_id>", methods=["GET"])
def get_courses_by_learner_id(learner_id):

    learner_class_list = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, enrolment_status="Enrolled", withdrawal=0).all()

    if len(learner_class_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_class": [learner_class.json() for learner_class in learner_class_list]
                }
            }
        )

    return jsonify(
            {
                "message": "Learner courses not found."
            }
        ), 404

# get all non-preassigned courses learner enrolled in using learner id
@app.route("/learner_class/withdrawal/<int:learner_id>", methods=["GET"])
def get_non_preassigned_courses_by_learner_id(learner_id):

    learner_class_list = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, enrolment_status="Enrolled", preassigned=0, withdrawal=0).all()
 
    if len(learner_class_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_class": [learner_class.json() for learner_class in learner_class_list]
                }
            }
        )
        

    return jsonify(
            {
                "message": "Learner courses not found."
            }
        ), 404

@app.route("/learner_class/inprogress/<int:learner_id>", methods=["GET"])
def get_inprogress_courses_by_learner_id(learner_id):

    class_inprogress = []
    learner_class_list = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, enrolment_status="Enrolled", withdrawal=0).all()

    if len(learner_class_list):
        for eachrow in learner_class_list:
        # if in the learner_class and progress less than 100, means in progress
            if eachrow.json()["progress"] < 100:
                class_inprogress.append(eachrow)

        return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "learner_class": [learner_class.json() for learner_class in class_inprogress]
                        }
                    }
                )

# learner_class/update_withdrawal/
# update withdrawal status
# only can withdraw if course is not preassigned by HR
# actually this one not used, if refactoring delete this
@app.route("/learner_class/update_withdrawal/<int:learner_id>/<string:course_name>", methods=["PUT"])
def update_withdrawal_status(learner_id, course_name):

    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, course_name=course_name, preassigned = 0).first()
    
    if learner_class:
        # data = request.get_json()
        # if data['withdrawal']:
        learner_class.withdrawal = True
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_class": learner_class.json()
                }
            }
        )

    return jsonify(
            {
                "code": 404,
                "data": {
                    "learner_id": learner_id,
                    "course_name": course_name
                },
                "message": "Learner or Class not found"
            }
        ), 404


@app.route("/learner_class/withdrawal_message/<int:learner_id>/<string:course_name>", methods=["PUT"])
def update_withdrawal_message(learner_id, course_name):

    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, course_name=course_name, preassigned = 0).first()
    
    if learner_class:
        data = request.get_json()
        # if data['withdrawal']:
        learner_class.withdrawal_message = data['withdrawal_message']
        learner_class.withdrawal = True
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_class": learner_class.json()
                }
            }
        )

    return jsonify(
            {
                "code": 404,
                "data": {
                    "learner_id": learner_id,
                    "course_name": course_name
                },
                "message": "Learner or Class not found"
            }
        ), 404


# get all pending records
@app.route("/pending", methods=["GET"])
def get_pending():

    pending_list = Learner_Class(db.Model).query.filter_by(enrolment_status="Pending").all()

    if pending_list:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "pending_list": [pending.json() for pending in pending_list]
                }
            }
        )

    return jsonify(
            {
                "message": "No pending requests."
            }
        ), 404

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

# test jenkin part 2
# update pending status
@app.route("/pending/<int:learner_id>/<string:course_name>", methods=["PUT"])
def update_pending(learner_id, course_name):

    learner_class = Learner_Class(db.Model).query.filter_by(learner_id=learner_id, course_name=course_name).first()
    
    if learner_class:
        data = request.get_json()
        if data['enrolment_status']:
            learner_class.enrolment_status = data['enrolment_status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "learner_class": learner_class.json()
                    }
                }
        )

    return jsonify(
            {
                "code": 404,
                "data": {
                    "learner_id": learner_id,
                    "course_name": course_name
                },
                "message": "Learner or Class not found"
            }
        ), 404

        
# get inclass count
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

# get inclass count with progress 100
@app.route("/class/count/completedCourse/<string:course_name>/<int:class_id>", methods=["GET"])
def get_inclass_count_completedcourse(course_name, class_id):

    get_inclass_count_completedcourse = Learner_Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id,enrolment_status="Enrolled",withdrawal=0, progress=100).all()

    if len(get_inclass_count_completedcourse):
        count = 0
        for learner in get_inclass_count_completedcourse:
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

@app.route("/learner_class/status/<string:course_name>/<int:class_id>/<int:learner_id>", methods=["GET"])
def get_status(course_name, class_id, learner_id):
    learner_class = Learner_Class(db.Model).query.filter_by(course_name=course_name, class_id=class_id, learner_id=learner_id).first()

    if learner_class:
        if (learner_class.enrolment_status == "Rejected"):
            return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "learner_class_status": "Rejected"
                        }
                    }
                )

        elif (learner_class.enrolment_status == "Pending"):
            return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "learner_class_status": "Pending"
                        }
                    }
                )
        else:
            return jsonify(
                        {
                            "code": 200,
                            "data": {
                                "learner_class_status": "Enrolled"
                            }
                        }
                    )
    return jsonify(
                {
                    "code": 200,
                    "data": {
                        "learner_class_status": "Not Enrolled"
                    }
                }
            )
            
# incourse regardless of class
@app.route("/class/<string:course_name>", methods=["GET"])
def get_incourse(course_name):

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

# inclass by course and class
@app.route("/class/<string:course_name>/<int:class_id>", methods=["GET"])
def get_inclass(course_name, class_id):

    inclass = Learner_Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id,enrolment_status="Enrolled",withdrawal=0).all()

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

# id in class 
@app.route("/class/<string:course_name>/<int:class_id>/<int:learner_id>", methods=["GET"])
def get_inclass_byid(course_name, class_id, learner_id):

    inclass = Learner_Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id,learner_id=learner_id,enrolment_status="Enrolled",withdrawal=0).first()

    if inclass:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inclass": inclass.json()
                }
            }
        )

    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "message": "Learner not enrolled in this class."
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


# enrol new learner into course

@app.route("/enrol/<string:course_name>/<int:class_id>/<int:learner_id>", methods=["POST"])
def hr_enrolment(course_name, class_id, learner_id):

    # check_current_count
    # inclass_count = Learner_Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id,enrolment_status="Enrolled",withdrawal=0).all()

    # if len(inclass_count):
    #     inclass_class_count = 0
    #     for learner in inclass_count:
    #         inclass_class_count += 1
    # else:
    #     inclass_class_count = 0

    # class size
    # class_size = Class(db.Model).query.filter_by(course_name=course_name,class_id=class_id).first()

    # if got capacity, add the learner
    new_enrolment = Learner_Class(course_name, class_id, learner_id, date.today(), 0, 'Enrolled', True, False)

    # if (inclass_class_count + 1 < class_size.class_size) {
    #     new_enrolment = ()
    # }

    # try:
    #     db.session.add(new_enrolment)
    #     db.session.commit()
    #     return jsonify({new_enrolment.to_dict()}), 201
    # except:
    #     return jsonify({
    #         "message": "Unable to commit to database."
    #     }), 500

    try:
        db.session.add(new_enrolment)
        db.session.commit()
        
        return jsonify (
            {
                "code": 201,
                "data": {
                    "new_enrolment": new_enrolment.json()
                },
                "message": "Enrolment commited to database."
            }
        ), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# @app.route("/enrol/learner", methods=['POST'])
# def enrol():
#     data = request.get_json()
#     if not all(key in data.keys() for
#                key in ('course_name', 'class_id', 'learner_id', 'date_assigned', 'start_date', 'end_date', 'progress', 'enrolment_status', 'preassigned', 'withdrawal')):
#         return jsonify({
#             "message": "Incorrect JSON object provided."
#         }), 500

#     # TO-DO: check if class exist first
#     # TO-DO: check if course created, then class can be created (?)
#     # currently request returns error "Unable to commit to database"

#     new_enrolment = Learner_Class(**data)
#     try:
#         db.session.add(new_enrolment)
#         db.session.commit()
#         return jsonify(new_enrolment.to_dict()), 201
#     except Exception:
#         return jsonify({
#             "message": "Unable to commit to database."
#         }), 500
    
@app.route("/enrol", methods=['POST'])
def engineer_enrolment():
    if request.method == 'POST':
        course_name= request.form['course_name']
        class_id = request.form['class_id']
        learner_id = request.form['learner_id']
        date_assigned = date.today()
        progress=request.form['progress']
        enrolment_status=request.form['enrolment_status']
        preassigned=False
        withdrawal=False

        newClass = Learner_Class(course_name=course_name, class_id=class_id, learner_id=learner_id,date_assigned=date_assigned,progress=progress,enrolment_status=enrolment_status,preassigned=preassigned,withdrawal=withdrawal)
        db.session.add(newClass)
        db.session.commit()
        return jsonify(newClass.__dict__), 201
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
