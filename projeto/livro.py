from projeto import db

class livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descrição = db.Column(db.String(100))
    valor = db.Column(db.Integer)
    def __init__(self, name, descrição, valor):
        self.name = name
        self.descrição = descrição
        self.valor = valor