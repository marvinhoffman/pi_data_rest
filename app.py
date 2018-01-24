from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.soil_moisture import SoilMoisture, SoilMoistureData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pi_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisasecretkey'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth (a new endpoint)

# Resources
api.add_resource(UserRegister, '/register')
api.add_resource(SoilMoisture, '/soildata')
api.add_resource(SoilMoistureData, '/soildataqry')

if __name__ == '__main__':
    from db import db # prevent infinte loop
    db.init_app(app)
    app.run(port=5080, debug=True)