from ma import ma
from models.book import BookModel

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        dump_only = ("id",)
        load_instance = True