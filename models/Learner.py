from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Engineer import Engineer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

# Learner inherits from Engineer
class Learner(Engineer):

    __tablename__ = 'learner'

    learner_id = db.Column(db.Integer, primary_key = True)
    engineer_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, engineer_id = "", learner_id = ""):
        super().__init__(engineer_id)
        self.learner_id = learner_id

    def get_learner_id(self):
        return self.learner_id

    def set_learner_id(self, learner_id):
        self.learner_id = learner_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)