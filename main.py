from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []

class Book(Resource):
    def get(self, title):
        book = next(filter(lambda x: x['title'] == title, books), None)
        return {'book': book}, 200 if book else 404

    def post(self, title):
        if next(filter(lambda x: x['title'] == title, books), None) is not None:
            return {'message':"A book with title '{}' already exists.".format(title)}, 400
        data = request.get_json()
        book = {'title':title, 'author':data['author'], 'year':data['year'], 'copies_sold':data['copies_sold']}
        books.append(book)
        return book, 201

    def delete(self, title):
        global books
        books = list(filter(lambda x: x['title'] != title, books))
        return {'message': 'Book deleted'}

    def put(self, title):
        data = request.get_json()
        book = next(filter(lambda x: x['title'] == title, books), None)
        if book is None:
            book = {'title':title, 'author':data['author'], 'year':data['year'], 'copies_sold':data['copies_sold']}
            books.append(book)
        else:
            book.update(data)
        return book

class BookList(Resource):
    def get(self):
        return {'books': books}

api.add_resource(Book, '/book/<string:title>') # http://localhost:5000/book/eragon
api.add_resource(BookList, '/books')

app.run(port=5000, debug=True)