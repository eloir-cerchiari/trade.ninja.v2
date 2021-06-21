from ..symbol import Symbol
from app import marshmallowInstance as ma



class SymbolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Symbol
