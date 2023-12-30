import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager() # Flask-Loginを使用するためのオブジェクトを生成

# ログイン関係の設定
login_manager.login_view = 'app.login' # ログインページのURLを指定
login_manager.login_message = 'ログインしてください' # ログインページのメッセージを指定

base_dir = os.path.abspath(os.path.dirname(__file__)) # 現在のディレクトリのパスを取得
db = SQLAlchemy() # dbオブジェクトを作成
migrate = Migrate() # migrateオブジェクトを作成

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret_key'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite') # data.sqliteのパスを設定
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 通知を有効化
  from flaskr.views import bp 
  app.register_blueprint(bp) # ブループリントを登録
  db.init_app(app) # dbオブジェクトを初期化
  migrate.init_app(app, db) # migrateオブジェクトを初期化
  login_manager.init_app(app) # Flask-Loginを初期化
  return app