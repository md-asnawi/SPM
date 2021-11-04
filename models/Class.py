# Class, part of Course

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Class(db.Model):

    __tablename__ = 'Class'
    __mapper_args__ = {'polymorphic_identity': 'Class'}

    course_name = db.Column(db.String(45), primary_key = True)
    class_id = db.Column(db.Integer, primary_key = True)
    class_size = db.Column(db.Integer, nullable = False)
    enrolment_start_date = db.Column(db.Date, nullable=False)
    enrolment_end_date = db.Column(db.Date, nullable=False)
    class_start_date = db.Column(db.Date, nullable = False)
    class_end_date = db.Column(db.Date, nullable = False)
    start_time = db.Column(db.Time, nullable = False)
    end_time = db.Column(db.Time, nullable = False)
    trainer_name = db.Column(db.String, nullable = False)

    def __init__(self, course_name, class_id, class_size, enrolment_start_date, enrolment_end_date, class_start_date, class_end_date, start_time, end_time, trainer_name):
        self.course_name = course_name
        self.class_id = class_id
        self.class_size = class_size
        self.enrolment_start_date = enrolment_start_date
        self.enrolment_end_date = enrolment_end_date
        self.class_start_date = class_start_date
        self.class_end_date = class_end_date
        self.start_time = start_time
        self.end_time = end_time
        self.trainer_name = trainer_name

    def json(self):
        return {
                "course_name": self.course_name, "class_id": self.class_id, "class_size": self.class_size,
                "enrolment_start_date": str(self.enrolment_start_date), "enrolment_end_date": str(self.enrolment_end_date),
                "class_start_date": str(self.class_start_date), "class_end_date": str(self.class_end_date), "start_time": str(self.start_time),
                "end_time": str(self.end_time), "trainer_name": self.trainer_name
        }

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name      

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id      

    def get_class_size(self):
        return self.class_size

    def set_class_size(self, class_size):
        self.class_size = class_size

    def get_enrolment_start_date(self):
        return self.enrolment_start_date

    def set_enrolment_start_date(self, enrolment_start_date):
        self.enrolment_start_date = enrolment_start_date

    def get_enrolment_end_date(self):
        return self.enrolment_end_date

    def set_enrolment_end_date(self, enrolment_end_date):
        self.enrolment_end_date = enrolment_end_date

    def get_class_start_date(self):
        return self.class_start_date

    def set_class_start_date(self, class_start_date):
        self.class_start_date = class_start_date

    def get_class_end_date(self):
        return self.class_end_date

    def set_class_end_date(self, class_end_date):
        self.class_end_date = class_end_date

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_trainer_name(self):
        return self.trainer_name

    def set_trainer_name(self, trainer_name):
        self.trainer_name = trainer_name

# db.create_all()

# GET all classes
@app.route("/class", methods=["GET"])
def get_all_classes():

    classList = Class.query.all()
    
    if len(classList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [single_class.json() for single_class in classList]
                }
            }
        )

# GET all classes in a course
@app.route("/class/<string:course_name>", methods=["GET"])
def get_all_classes_in_course(course_name):

    classList = Class.query.filter_by(course_name = course_name).all()

    if len(classList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "classes": [single_class.json() for single_class in classList]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    )


# GET 1 class given course name & class id
@app.route("/class/<string:course_name>/<int:class_id>", methods=["GET"])
def get_one_class(course_name, class_id):

    single_class = Class.query.filter_by(course_name = course_name, class_id = class_id).first()

    if single_class:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "single_class": single_class.json()
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Class not found."
        }
    )

# CREATE new class
@app.route("/class", methods=['POST'])
def create_class():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('course_name', 'class_id', 'class_size', 
                       'enrolment_start_date', 'enrolment_end_date',
                       'class_start_date', 'class_end_date', 
                       'start_time', 'end_time', 'trainer_name')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # TO-DO: check if class exist first
    # TO-DO: check if course created, then class can be created (?)
    # currently request returns error "Unable to commit to database"

    new_class = Class(**data)
    try:
        db.session.add(new_class)
        db.session.commit()
        return jsonify(new_class.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
    