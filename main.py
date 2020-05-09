from flask import Flask
from flask_restful import Api
from book import Book, BookList

app = Flask(__name__)
api = Api(app)

api.add_resource(Book, '/book/<string:title>') # http://localhost:5000/book/eragon
api.add_resource(BookList, '/books')

if __name__ == '__main__':
    app.run(port=5000, debug=True)