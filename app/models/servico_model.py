from app import db

class Servico(db.Model):
    __tablename__ = "servico"
  
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    etapa  = db.Column(db.String(200))
    situacao  = db.Column(db.String(200))
    codigo_rastreio  = db.Column(db.String(200))
    data_entrada  = db.Column(db.String(200))