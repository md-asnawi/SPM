from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from learner_class import Learner_Class
from material import Material

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Learner_Material(db.Model):

    __tablename__ = 'learner_material'
    __mapper_args__ = {'polymorphic_identity': 'learner_material'}

    course_name = db.Column(db.String(45),db.ForeignKey(Material.course_name), nullable=False, primary_key = True)
    class_id = db.Column(db.Integer, db.ForeignKey(Material.class_id), primary_key = True)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Material.lesson_id), primary_key = True)
    material_id = db.Column(db.Integer, db.ForeignKey(Material.material_id), primary_key = True)
    learner_id = db.Column(db.Integer, db.ForeignKey(Learner_Class.learner_id), nullable=False, primary_key = True)
    completion_status = db.Column(db.String(45), nullable=False)
    
    def __init__(self, course_name, class_id, lesson_id, material_id, learner_id, completion_status):
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.material_id = material_id
        self.learner_id = learner_id
        self.completion_status = completion_status

    def json(self):
        return{
            "course_name": self.course_name, "class_id": self.class_id, "lesson_id": self.lesson_id,
            "material_id": self.material_id, "learner_id": self.learner_id, "completion_status": self.completion_status
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
        return self.course_name

    def set_lesson_id(self, lesson_id):
        self.lesson_id = lesson_id

    def get_material_id(self):
        return self.material_id

    def set_material_id(self, material_id):
        self.material_id = material_id

    def get_learner_id(self):
        return self.learner_id

    def set_learner_id(self, learner_id):
        self.learner_id = learner_id

    def get_completion_status(self):
        return self.completion_status

    def set_completion_status(self, completion_status):
        self.completion_status = completion_status

# get all learner_material
@app.route("/learner_material", methods=["GET"])
def get_all_learner_material():

    learner_material_list = Learner_Material.query.all()
    
    if len(learner_material_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_material": [learner_material.json() for learner_material in learner_material_list]
                }
            }
        )

    return jsonify(
        {
            "message": "No learner material found."
        }
    ), 404


# get all learner_materials using course_name, class_id, lesson_id, material_id, learner_id
@app.route("/learner_material/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:material_id>/<int:learner_id>", methods=["GET"])
def get_all_learner_material_of_learner_and_lesson(course_name, class_id, lesson_id, material_id, learner_id):

    learner_material_list = Learner_Material.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id,
                                                             material_id = material_id, learner_id = learner_id).all()
    
    if len(learner_material_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_material": [learner_material.json() for learner_material in learner_material_list]
                }
            }
        )

    return jsonify(
        {
            "message": "Learner Material not found."
        }
    ), 404

# get all COMPLETED/UNCOMPLETED learner_materials using course_name, class_id, lesson_id, material_id, learner_id, completion_status
@app.route("/learner_material/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:material_id>/<int:learner_id>/<string:completion_status>", methods=["GET"])
def get_all_learner_material_of_learner_and_lesson_and_completion_status(course_name, class_id, lesson_id, material_id, learner_id, completion_status):

    learner_material_list = Learner_Material.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id,
                                                             material_id = material_id, learner_id = learner_id, completion_status = completion_status).all()
    
    if len(learner_material_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner_material": [learner_material.json() for learner_material in learner_material_list]
                }
            }
        )

    return jsonify(
        {
            "message": "No " + completion_status + " learner material found"
        }
    ), 404

# update completion status
@app.route("/learner_material/<string:course_name>/<int:class_id>/<int:lesson_id>/<int:material_id>/<int:learner_id>", methods=["PUT"])
def update_learner_material_completion(course_name, class_id, lesson_id, material_id, learner_id):

    learner_material = Learner_Material.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id, material_id = material_id, learner_id = learner_id).first()
    
    if learner_material:
        data = request.get_json()
        if data['completion_status']:
            learner_material.enrolment_status = data['completion_status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "learner_material": learner_material.json()
                    }
                }
        )

    return jsonify(
            {
                "code": 404,
                "data": {
                    "course_name": course_name,
                    "class_id": class_id,
                    "lesson_id": lesson_id,
                    "material_id": material_id,
                    "learner_id": learner_id
                },
                "message": "Learner Material not found"
            }
        ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
