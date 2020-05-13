from flask import Flask, jsonify
from flask_restful import Api
from resources.book import Book, BookList
from config import configuration
from db import db
from ma import ma
from marshmallow import ValidationError

# Configuration
conf = configuration("./config.ini")
api_port = conf.get('server','port')
debug_mode = conf.get('server','debug')
database_uri = conf.get('database','database_uri')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

api.add_resource(Book, '/book/<string:title>') # http://localhost:5000/book/eragon
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=api_port, debug=debug_mode)