# Engineer
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100, 'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Engineer(db.Model):

    __tablename__ = 'engineer'

    engineer_id = db.Column(db.Integer, primary_key = True)
    engineer_name = db.Column(db.String(45), nullable=False)
    
    def __init__(self, name = "", engineer_id = ""):
        self.name = name
        self.engineer_id = engineer_id

    def json(self):
        return{"engineer_id": self.engineer_id, "engineer_name": self.engineer_name}

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_engineer_id(self):
        return self.engineer_id

    def set_engineer_id(self, engineer_id):
        self.engineer_id = engineer_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)