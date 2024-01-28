from flaskr import db, login_manager # flaskr/__init__.pyのdbとlogin_managerをインポート
from flask_bcrypt import generate_password_hash, check_password_hash # パスワードのハッシュ化とチェックのためにインポート
from flask_login import UserMixin # ログイン機能のためにインポート
from datetime import datetime , timedelta # 日付と時刻のためにインポート
from uuid import uuid4 # UUIDを生成するためにインポート、UUIDはユニバーサルユニーク識別子のこと、パスワードの発行に使用する


@login_manager.user_loader # ログインマネージャーのユーザーをロードするためのデコレーター
def load_user(user_id):
  return User.query.get(user_id)


class User(UserMixin, db.Model):
  # db.Modelを継承してSQLAlchemyを使用したDBモデルを作成
  # UserMixinを継承してログイン機能を追加
  
  __tablename__ = 'users' # テーブル名を指定
  
  id = db.Column(db.Integer, primary_key=True) # ユーザーID
  username = db.Column(db.String(64),  index=True) # ユーザー名
  email = db.Column(db.String(64), unique=True, index=True) # メールアドレス
  password = db.Column(
    db.String(128),
    default=generate_password_hash('snsflaskapp'),
  ) # パスワード
  picture_path  = db.Column(db.Text) # プロフィール画像のパス
  is_active = db.Column(db.Boolean, default=False) # ユーザーがアクティブかどうか
  created_at = db.Column(db.DateTime, default=datetime.now) # ユーザーの作成日時
  updated_at = db.Column(db.DateTime, default=datetime.now) # ユーザーの更新日時
  
  
# パスワードリセット時に使用する
class PasswordResetToken(db.Model):
  
  __tablaename__ = 'password_reset_tokens'
  
  id = db.Column(db.Integer, primary_key=True) # ID
  token = db.Column(
    db.String(64), 
    unique=True, 
    index=True,
    server_default=str(uuid4) # UUIDを生成、str()で文字列に変換
    ) 
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # ユーザーID、usersテーブルのidカラムとリレーションする
  expired_at = db.Column(db.DateTime, default=datetime.now) # トークンの有効期限
  created_at = db.Column(db.DateTime, default=datetime.now) # パスワードリセットトークンの作成日時
  updated_at = db.Column(db.DateTime, default=datetime.now) # パスワードリセットトークンの更新日時
  
  