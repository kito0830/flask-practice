from flaskr import db, login_manager # flaskr/__init__.pyのdbとlogin_managerをインポート
from flask_bcrypt import generate_password_hash, check_password_hash # パスワードのハッシュ化とチェックのためにインポート
from flask_login import UserMixin # ログイン機能のためにインポート
from datetime import datetime , timedelta # 日付と時刻のためにインポート
from uuid import uuid4 # UUIDを生成するためにインポート、UUIDはユニバーサルユニーク識別子のこと、パスワードの発行に使用する


@login_manager.user_loader # ログインマネージャーのユーザーをロードするためのデコレーター
