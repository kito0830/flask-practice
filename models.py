from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app # app.pyからappオブジェクトをインポート

db = SQLAlchemy(app)
Migrate(app, db)

class Member(db.Model):
  __tablename__ = 'members' # テーブル名を設定
  id = db.Column(db.Integer, primary_key=True) # idカラム
  name = db.Column(db.Text) # nameカラム
  age = db.Column(db.Integer) # ageカラム
  comment = db.Column(db.Text) # commentカラム
  
  # インスタンス作成時に呼ばれるメソッド
  def __init__(self, name, age, comment):
    self.name = name
    self.age = age
    self.comment = comment
  