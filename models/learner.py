from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from engineer import Engineer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

# Learner inherits from Engineer
class Learner(Engineer):

    __tablename__ = 'learner'
    __mapper_args__ = {'polymorphic_identity': 'learner'}

    learner_id = db.Column(db.Integer, primary_key = True)
    engineer_id = db.Column(db.Integer, db.ForeignKey(Engineer.engineer_id), nullable=False)
    
    def __init__(self, engineer_name, engineer_id = "", learner_id = ""):
        super().__init__(engineer_name, engineer_id)
        self.learner_id = learner_id

    def json(self):
        return{"engineer_id": self.engineer_id, "engineer_name": self.engineer_name, "learner_id": self.learner_id}

    def get_learner_id(self):
        return self.learner_id

    def set_learner_id(self, learner_id):
        self.learner_id = learner_id
        
# get all learners
@app.route("/all", methods=["GET"])
def get_all_learners():

    learnerlist = Learner.query.all()
    
    if len(learnerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner": [learner.json() for learner in learnerlist]
                }
            }
        )

# get a learner using learner id
@app.route("/learner/<int:learner_id>", methods=["GET"])
def get_learner_by_id(learner_id):

    learner = Learner.query.filter_by(learner_id = learner_id).first()
    
    if learner:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner": learner.json()
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Learner not found."
        }
    ), 404

# get a learner using learner name
@app.route("/learner/<string:engineer_name>", methods=["GET"])
def get_learner_byname(engineer_name):

    learner = Learner.query.filter_by(engineer_name = engineer_name).first()
    
    if learner:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "learner": learner.json()
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "Learner not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
