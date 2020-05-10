import sqlite3
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
            book.insert()
        except:
            return {"message":"An error ocurred inserting the book."}, 500

        return book.json(), 201

    def delete(self, title):
        
        book = BookModel.find_by_title(title)

        if book:

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM books WHERE title = ?"
            cursor.execute(query, (title,))

            connection.commit()
            connection.close()

            return {'message': 'Book deleted'}

        return {'message':'This book does not exist.'}, 400

    def put(self, title):
        
        data = request.get_json()

        try:
            book = BookModel.find_by_title(title)
        except:
            return {"message":"An error courred searching for the book"},500

        updated_book = BookModel(title,data['author'],data['year'],data['copies_sold'])

        if book is None:
            try:
                book.insert()
            except:
                return {"message":"An error ocurred inserting the book"},500
        else:
            try:
                book.update()
            except:
                return {"message":"An error ocurred updating the book"},500

        return updated_book.json()


class BookList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM books"
        result = cursor.execute(query)

        books = []
        for row in result:
            books.append({'title':row[0],'author':row[1],'year':row[2], 'copies_sold':row[3]})

        connection.close()

        return {'books':books}