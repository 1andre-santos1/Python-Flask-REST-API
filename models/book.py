import sqlite3

class BookModel:
    def __init__(self, title, author, year, copies_sold):
        self.title = title
        self.author = author
        self.year = year
        self.copies_sold = copies_sold

    def json(self):
        return {'title':self.title, 'author': self.author, 'year':self.year, 'copies_sold':self.copies_sold}

    @classmethod
    def find_by_title(cls, title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM books WHERE title =?"
        result = cursor.execute(query, (title,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
    
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO books VALUES (?, ?, ?, ?)"
        cursor.execute(query, (self.title, self.author, self.year, self.copies_sold))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE books SET title=?,author=?,year=?,copies_sold=? WHERE title=?"
        cursor.execute(query, (self.title, self.author, self.year, self.copies_sold,self.title))

        connection.commit()
        connection.close()