from flask import request
from flask_restful import Resource
from models.book import BookModel
from schemas.book import BookSchema
from marshmallow import ValidationError

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)

class Book(Resource):
    def get(self, title):
        try:
            book = BookModel.find_by_title(title)
        except:
            return {"message":"An error ocurred while searching for the book."}, 500
        
        if book:
            return book_schema.dump(book), 200
        return {'message': 'Book not found'}, 404

    def post(self, title):

        if BookModel.find_by_title(title):
          return {'message':"A book with title '{}' already exists.".format(title)}, 400
        
        data = book_schema.load(request.get_json())

        try:
            data.save_to_db()
        except:
            return {"message":"An error ocurred inserting the book."}, 500

        return book_schema.dump(data), 201

    def delete(self, title):
        
        book = BookModel.find_by_title(title)

        if book:

            book.delete_from_db()

            return {'message': 'Book deleted'}, 204

        return {'message':'This book does not exist.'}, 400

    def put(self, title):
        
        data = book_schema.load(request.get_json())

        book = BookModel.find_by_title(title)
        
        if book is None:
            book = BookModel(title, data.author, data.year, data.copies_sold)
        else:
            book.author = data['author']
            book.year = data['year']
            book.copies_sold = data['copies_sold']

        book.save_to_db()

        return book_schema.dump(book), 200


class BookList(Resource):
    def get(self):
        return {'books': book_list_schema.dump(BookModel.find_all())}, 200