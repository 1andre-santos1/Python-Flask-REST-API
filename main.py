from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Book(Resource):
    def get(self, title):
        return {'book' : title}

api.add_resource(Book, '/book/<string:title>') # http://localhost:5000/book/eragon

app.run(port=5000)