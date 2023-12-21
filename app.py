import os
from flask import Flask

app = Flask(__name__)
base_dir = os.path.dirname(__file__) #現在のディレクトリのパスを取得

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite') # data.sqliteのパスを設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 通知を有効化