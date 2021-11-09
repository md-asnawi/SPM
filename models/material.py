from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from lesson import Lesson

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:WxJJy9gTnsC9@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Material(db.Model):

    material_id = db.Column(db.Integer, primary_key = True)
    material_name = db.Column(db.String(45), nullable = True)
    format = db.Column(db.String(45), nullable = True)
    material_type = db.Column(db.String(45), nullable = True)
    uploader = db.Column(db.Integer, nullable = False)
    course_name = db.Column(db.String(45), db.ForeignKey(Lesson.course_name), nullable = False)
    class_id = db.Column(db.Integer, db.ForeignKey(Lesson.class_id), nullable = False)
    lesson_id = db.Column(db.Integer, db.ForeignKey(Lesson.lesson_id), nullable = False)

    def __init__(self, material_id, material_name, format, material_type, uploader, course_name, class_id, lesson_id):
        self.material_id = material_id
        self.material_name = material_name
        self.format = format
        self.material_type = material_type
        self.uploader = uploader
        self.course_name = course_name
        self.class_id = class_id
        self.lesson_id = lesson_id

    def json(self):
        return {
                "material_id": self.material_id, "material_name": self.material_name, "format": self.format, 
                "material_type": self.material_type, "uploader": self.uploader, "course_name": self.course_name, 
                "class_id": self.class_id, "lesson_id": self.lesson_id
        }

    def get_material_id(self):
        return self.material_id

    def set_material_id(self, material_id):
        self.material_id = material_id

    def get_material_name(self):
        return self.material_name

    def set_material_name(self, material_name):
        self.material_name = material_name

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    def get_material_type(self):
        return self.material_type

    def set_material_type(self, material_type):
        self.material_type = material_type

    def get_uploader(self):
        return self.uploader

    def set_uploader(self, uploader):
        self.uploader = uploader

# GET all materials
@app.route("/material", methods=["GET"])
def get_all_materials():

    materialList = Material.query.all()  
    
    if len(materialList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": [material.json() for material in materialList]
                }
            }
        )

    return jsonify(
        {
            "message": "No material found."
        }
    ), 404

# GET materials with material id
@app.route("/material/<int:material_id>", methods=["GET"])
def get_material(material_id):

    material = Material.query.filter_by(material_id = material_id).first()
    
    if material:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": material.json()
                }
            }
        )

    return jsonify(
        {
            "message": "Material not found."
        }
    ), 404

# GET all materials in 1 lesson with course id, class id, lesson id
@app.route("/material/<string:course_name>/<int:class_id>/<int:lesson_id>", methods=["GET"])
def get_materials_of_lesson(course_name, class_id, lesson_id):

    materialList = Material.query.filter_by(course_name = course_name, class_id = class_id, lesson_id = lesson_id).all()
    
    if len(materialList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "material": [material.json() for material in materialList]

                }
            }
        )

    return jsonify(
        {
            "message": "Material not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
