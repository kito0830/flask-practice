from wtforms.form import Form
from wtforms.fields import StringField, SubmitField, IntegerField, TextAreaField, HiddenField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User # このファイルの中にあるUserクラスをインポート

# ログインフォームで使用
class LoginForm(Form):
  # ログインフォーム
  email = StringField('メールアドレス', validators=[DataRequired(), Email()])
  password = PasswordField('パスワード', validators=[DataRequired()])
  submit = SubmitField('ログイン')
  
# ユーザー登録フォームで使用 
class RegisterForm(Form):
  email = StringField('メール：', validators=[DataRequired(), Email()])
  username = StringField('名前：', validators=[DataRequired()])
  password = PasswordField('パスワード：', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しません')])
  password_confirm = PasswordField('パスワード確認：', validators=[DataRequired()])
  submit = SubmitField('登録')
  
# メールアドレスの重複チェック
def validate_email(self, field):
  if User.select_by_email(field.data):
    raise ValidationError('そのメールアドレスは既に登録されています')