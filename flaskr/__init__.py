import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

login_manager = LoginManager()
login_manager.login_view = 'app.view'
login_manager.login_message = 'ログインしてください'

basedir = os.path.abspath(os.path.dirname(__name__)) # 現在のディレクトリの絶対パスを取得
db = SQLAlchemy() # SQLAlchemyのインスタンスを生成
migrate = Migrate()

def create_app():
  app = Flask(__name__) # Flaskのインスタンスを生成、__name__は現在のファイルの名前
  app.config['SECRET_KEY'] = 'mysite'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') # データベースのURIを指定ファイル名の末尾にdata.sqliteを指定
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemyの追跡機能をオフにする
  from flaskr.views import bp
  app.register_blueprint(bp) # ブループリントを登録
  db.init_app(app) # SQLAlchemyの初期化、アプリケーションがデータベースを使用できるようになる
  migrate.init_app(app, db) # マイグレーションの初期化、
  login_manager.init_app(app) # ログインマネージャーの初期化
  
  #この関数を呼び出すことで、アプリケーションが起動し、設定された機能が有効になります。
  # 通常、この関数はFlaskアプリケーションのエントリーポイントとして使用されます。
  return app