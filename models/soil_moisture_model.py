from db import db
from dateutil import parser

class SoilMoistureModel(db.Model):
    __tablename__ = 'soilmoisture'

    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.Float(precision=5))
    timestamp = db.Column(db.DateTime)


    def __init__(self, voltage, timestamp):
        self.voltage = voltage
        self.timestamp = parser.parse(timestamp)


    def json(self):
        return {'voltage': self.voltage, 'timestamp': str(self.timestamp)}


    def save_data(self):
        db.session.add(self)
        db.session.commit()


    def remove_data(self):
        db.session.delete(self)
        db.session.commit()
