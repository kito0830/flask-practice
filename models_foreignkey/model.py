import os
from flask import Flask # Flaskのインポート
from flask_sqlalchemy import SQLAlchemy # SQLAlchemyのインポート

base_dir = os.path.dirname(__file__) # model.pyを配置しているファイルパス

app = Flask(__name__) # Flaskオブジェクトの作成
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite') # sqliteのDBのパスを設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 通知を抑制
app.config['SQLALCHEMY_ECHO'] = True # ターミナルに実行したSQLを出力

db = SQLAlchemy(app) # dbオブジェクトを作成

class Employee(db.Model):
  __tablename__ = 'employees' # テーブル名を設定
  
  id = db.Column(db.Integer, primary_key=True) # idカラム
  name = db.Column(db.Text) # nameカラム
  
  # 1対多のリレーションを設定
  projects = db.relationship('Project', backref='employees') # Projectモデルとのリレーションを設定
  
  # 1対1のリレーションを設定
  company =  db.relationship('Company', backref='employees', uselist=False) # Companyモデルとのリレーションを設定
  
  # backref = 双方向リレーションを設定をしてくれる
  
  def __init__(self, name) :
    self.name = name
    
  def __str__(self): 
    if self.company:
      return f"id = {self.id}, name = {self.name}, company = {self.company.name}"
    else:
      return f"id = {self.id}, name = {self.name}, company = None"
  
  def show_projects(self):
    for project in self.projects:
      print(project)
      
      
# Projectモデルを作成
class Project(db.Model):
  __tablename__ = 'projects' # テーブル名を設定 
  
  id = db.Column(db.Integer, primary_key=True) # idカラム
  name = db.Column(db.Text) # nameカラム
  employee_id = db.Column(db.Integer, db.ForeignKey('employees.id')) # employeesテーブルの外部キーを設定
  
  def __init__(self, name, employee_id):
    self.name = name
    self.employee_id = employee_id
    

class Company(db.Model):
  __tablename__ = 'companies' # テーブル名を設定
  
  id = db.Column(db.Integer, primary_key=True) # idカラム
  name = db.Column(db.Text) # nameカラム
  employee_id = db.Column(db.Integer, db.ForeignKey('employees.id')) # employeesテーブルの外部キーを設定
  
  def __init__(self, name, employee_id):
    self.name = name
    self.employee_id = employee_id

with app.app_context():
  db.create_all() # テーブルを作成