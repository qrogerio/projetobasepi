from app import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(200))
    telefone = db.Column(db.Integer)
    email = db.Column(db.String(200))