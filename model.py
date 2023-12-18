import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, CheckConstraint

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  __table_args__ = (
    CheckConstraint('update_at >= created_at'), # created_atよりもupdate_atが大きいことを保証
  )

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), index=True, server_default='nanashi')
  phone_number = db.Column(db.String(13), unique=True, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime)
  update_at = db.Column(db.DateTime)

  def __init__(self, name, phone_number, age, created_at, update_at):
    self.name = name
    self.phone_number = phone_number
    self.age = age
    self.created_at = created_at
    self.update_at = update_at

  def __str__(self): # __repr__でも可
    return f"id = {self.id}, name = {self.name}, phone_number = {self.phone_number}, age = {self.age}, created_at = {self.created_at}, update_at = {self.update_at}"
  
with app.app_context():
  db.Index('my_index', func.lower(Person.name)) # nameカラムを小文字に変換してインデックスを作成（小文字の検索が早くなる）
  db.create_all() # テーブルを作成