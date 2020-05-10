from db import db

class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    author = db.Column(db.String(250))
    year = db.Column(db.Integer)
    copies_sold = db.Column(db.Integer)

    def __init__(self, title, author, year, copies_sold):
        self.title = title
        self.author = author
        self.year = year
        self.copies_sold = copies_sold

    def json(self):
        return {'title':self.title, 'author': self.author, 'year':self.year, 'copies_sold':self.copies_sold}

    @classmethod
    def find_by_title(cls, title):
        return BookModel.query.filter_by(title=title).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()