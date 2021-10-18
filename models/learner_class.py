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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Class(db.Model):

    __tablename__ = 'learner_class'

    course_name = db.Column(db.String(45),db.ForeignKey(Class.course_name), nullable=False, primary_key = True)
    class_id = db.Column(db.Integer,db.ForeignKey(Class.class_id), primary_key = True)
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

@app.route("/enrol", methods=['POST'])
def enrolment():
    if request.method == 'POST':
        course_name= request.form['course_name']
        class_id = request.form['class_id']
        learner_id = request.form['learner_id']
        date_assigned = date.today()
        start_date = db.session.query(Class.start_date).filter(Class.course_name.like(course_name), Class.class_id.like(class_id))
        end_date=db.session.query(Class.end_date).filter(Class.course_name.like(course_name), Class.class_id.like(class_id))
        progress=request.form['progress']
        enrolment_status=request.form['enrolment_status']
        preassigned=False
        withdrawal=False

        newClass = Learner_Class(course_name=course_name, class_id=class_id, learner_id=learner_id,date_assigned=date_assigned,start_date=start_date,end_date=end_date,progress=progress,enrolment_status=enrolment_status,preassigned=preassigned,withdrawal=withdrawal)
        db.session.add(newClass)
        db.session.commit()
        return jsonify(newClass.__dict__), 201
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)