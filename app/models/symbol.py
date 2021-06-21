from app import sqlAlchemyInstance as db , marshmallowInstance as ma

class Symbol(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol=db.Column(db.String,  nullable=False)
    exchange=db.Column(db.String,  nullable=False)
    screener=db.Column(db.String, nullable=False)
    interval=db.Column(db.String, nullable=False)
    lastUpdate=db.Column(db.DateTime, nullable=True)
    recommendation=db.Column(db.String,  nullable=True)
    active = db.Column(db.Boolean, nullable = True)




    def __init__(self, symbol, exchange, screener, interval, lastUpdate = None, recommendation = None):
        self.symbol  = symbol
        self.exchange = exchange
        self.screener = screener
        self.interval = interval
        self.lastUpdate = lastUpdate
        self.recommendation = recommendation




# outra opção        
# class SymbolSchema(ma.Schema):
#     class Meta:
#         fields = ('id','symbol', 'exchange', 'screener', 'interval', 'lastUpdate', 'recommendation')