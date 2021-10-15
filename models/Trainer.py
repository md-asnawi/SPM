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

# Trainer inherits from Engineer
class Trainer(Engineer):

    __tablename__ = 'trainer'
    __mapper_args__ = {'polymorphic_identity': 'trainer'}

    trainer_id = db.Column(db.Integer, primary_key = True)
    engineer_id = db.Column(db.Integer, db.ForeignKey(Engineer.engineer_id), nullable=False)

    def __init__(self, engineer_id = "", trainer_id = ""):
        super().__init__(engineer_id)
        self.trainer_id = trainer_id

    def json(self):
        return{"engineer_id": self.engineer_id, "engineer_name": self.engineer_name, "trainer_id": self.trainer_id}

    def get_trainer_id(self):
        return self.trainer_id

    def set_trainer_id(self, trainer_id):
        self.trainer_id = trainer_id

@app.route("/all", methods=["GET"])
def get_all():

    trainerlist = Trainer.query.all()
    
    if len(trainerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "trainer": [trainer.json() for trainer in trainerlist]
                }
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)