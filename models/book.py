from db import db

class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250))
    year = db.Column(db.Integer)
    copies_sold = db.Column(db.Integer)

    @classmethod
    def find_by_title(cls, title):
        return BookModel.query.filter_by(title=title).first()

    @classmethod
    def find_all(cls):
        return BookModel.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()