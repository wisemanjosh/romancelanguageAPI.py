from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Romancelanguage(Resource):
    def get(self):
        return {'FirstRomancelanguage': 'Sicilian', 'Region': 'Italy', 'Language Origin': 'Latin, Greek, Arabic', 'Languages influenced': 'French, Catalan, and Spanish', 'Age of the language': '700 years a.D'}

api.add_resource(Romancelanguage, '/')

if __name__ == '__main__':
    app.run(debug=True)

