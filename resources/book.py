from flask import request
from flask_restful import Resource
from models.book import BookModel

class Book(Resource):
    def get(self, title):
        try:
            book = BookModel.find_by_title(title)
        except:
            return {"message":"An error ocurred while searching for the book."}, 500
        
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    def post(self, title):

        if BookModel.find_by_title(title):
          return {'message':"A book with title '{}' already exists.".format(title)}, 400
        
        data = request.get_json()

        book = BookModel(title, data['author'], data['year'], data['copies_sold'])
        
        try:
            book.save_to_db()
        except:
            return {"message":"An error ocurred inserting the book."}, 500

        return book.json(), 201

    def delete(self, title):
        
        book = BookModel.find_by_title(title)

        if book:

            book.delete_from_db()

            return {'message': 'Book deleted'}

        return {'message':'This book does not exist.'}, 400

    def put(self, title):
        
        data = request.get_json()

        book = BookModel.find_by_title(title)
        
        if book is None:
            book = BookModel(title, data['author'], data['year'], data['copies_sold'])
        else:
            book.author = data['author']
            book.year = data['year']
            book.copies_sold = data['copies_sold']

        book.save_to_db()

        return book.json()


class BookList(Resource):
    def get(self):
        return {'books':[book.json() for book in BookModel.query.all()]}