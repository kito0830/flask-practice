import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# model.pyを配置しているファイルパス
base_dir = os.path.dirname(__file__)

app = Flask(__name__)

# sqliteのDBのパスを設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 通知を抑制

#dbオブジェクトを作成
db = SQLAlchemy(app) 

class Person(db.Model):
     __tablename__ = 'persons' # テーブル名を設定
     id = db.Column(db.Integer, primary_key=True) # idカラム
     name = db.Column(db.Text) # nameカラム
     age = db.Column(db.Integer) # ageカラム

     def __init__(self, name, age):
          self.name = name
          self.age = age
      
     def __str__(self):
        return f"id = {self.id}, name = {self.name}, age = {self.age}"