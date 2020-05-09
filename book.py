import sqlite3
from flask import request
from flask_restful import Resource

class Book(Resource):
    def get(self, title):
        try:
            book = self.find_by_title(title)
        except:
            return {"message":"An error ocurred while searching for the book."}, 500
        
        if book:
            return book
        return {'message': 'Book not found'}, 404

    @classmethod
    def find_by_title(cls, title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM books WHERE title =?"
        result = cursor.execute(query, (title,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'book':{'title':row[0],'author':row[1],'year':row[2],'copies_sold':row[3]}}
        

    def post(self, title):

        if self.find_by_title(title):
          return {'message':"A book with title '{}' already exists.".format(title)}, 400
        
        data = request.get_json()

        book = {'title':title, 'author':data['author'], 'year':data['year'], 'copies_sold':data['copies_sold']}
        
        try:
            self.insert(book)
        except:
            return {"message":"An error ocurred inserting the book."}, 500

        return book, 201

    @classmethod
    def insert(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO books VALUES (?, ?, ?, ?)"
        cursor.execute(query, (book['title'], book['author'], book['year'], book['copies_sold']))

        connection.commit()
        connection.close()

    def delete(self, title):
        
        book = self.find_by_title(title)

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
            book = self.find_by_title(title)
        except:
            return {"message":"An error courred searching for the book"},500

        updated_book = {'title':title, 'author':data['author'], 'year':data['year'], 'copies_sold':data['copies_sold']}

        if book is None:
            try:
                self.insert(updated_book)
            except:
                return {"message":"An error ocurred inserting the book"},500
        else:
            try:
                self.update(updated_book)
            except:
                return {"message":"An error ocurred updating the book"},500

        return updated_book

    @classmethod
    def update(cls, book):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE books SET title=?,author=?,year=?,copies_sold=? WHERE title=?"
        cursor.execute(query, (book['title'], book['author'], book['year'], book['copies_sold'],book['title']))

        connection.commit()
        connection.close()

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