import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager() # Flask-Loginを使用するためのオブジェクトを生成

# ログイン関係の設定
login_manager.login_view = 'app.login' # ログインページのURLを指定
login_manager.login_message = 'ログインしてください' # ログインページのメッセージを指定

base_dir = os.path.abspath.(os.path.dirname(__file__)) # 現在のディレクトリのパスを取得
db = SQLAlchemy(app) # dbオブジェクトを作成