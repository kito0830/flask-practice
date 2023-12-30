from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin


# セッションに保存されたログインユーザーを変えるためにtemplateから呼ばれる
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# UserMixinを継承することで、Userクラスにログインユーザーの情報を取得するためのメソッドが追加される
class User(db.Model, UserMixin):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), index=True)
  password = db.Column(db.String(128))
  
  def __init__(self, email, username, password):
    self.email = email
    self.username = username
    self.password = generate_password_hash(password) # パスワードをハッシュ化して保存
    
  def validate_password(self, password):
    return check_password_hash(self.password, password)
  
  def add_user(self):
    with db.session.begin():
      db.session.add(self)
    db.session.commit()
    
  @classmethod
  def select_by_email(cls, email):
    return cls.query.filter_by(email=email).first()
 