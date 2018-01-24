from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from dateutil import parser

from models.soil_moisture_model import SoilMoistureModel

class SoilMoisture(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('voltage',
        type=float,
        required=False,
        help='A voltage measurement is required.')
    parser.add_argument('timestamp',
        type=str,
        required=False,
        help='A timestamp measurement is required.')

    @jwt_required()
    def get(self):
        return {"voltage": "voltage goes here"}

    @jwt_required()
    def post(self):
        data = SoilMoisture.parser.parse_args()
        py_timestamp = parser.parse(data['timestamp'])
        moisture_measurement = SoilMoistureModel(data['voltage'], str(py_timestamp)) # **data
        moisture_measurement.save_data()
        # try:
        #     moisture_measurement.save_data()
        # except:
        #     return {'message': 'An error has occurred saving data.'}, 500

        return moisture_measurement.json(), 201


class SoilMoistureData(Resource):
    @jwt_required()
    def get(self):
        return {'Soil Data': [soildata.json() for soildata in SoilMoistureModel.query.all()]}
