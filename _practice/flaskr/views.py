from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user
from flaskr.forms import LoginForm, RegisterForm
from flaskr.models import User

bp = Blueprint('app', __name__, url_prefix='') # url_prefixを指定

@bp.route('/')
def home():
  return render_template('home.html')

@bp.route('/welcome')
@login_required # ログインしていないとアクセスできない(login_userが実行されていないと)
# ログインしていない場合は、ログインページにリダイレクトされる
def welcome():
  return render_template('welcome.html')

@bp.route('/logout')
@login_required # ログインしていないとアクセスできない(login_userが実行されていないと)
def logout():
  logout_user() # ログアウト処理
  return redirect(url_for('app.home'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
  flash('This is a flash message', 'success')
  form = LoginForm(request.form)
  if request.method == 'POST' and form.validate():  
    user = User.select_by_email(form.email.data) 
    # 上記で取得したuserのパスワードとクライアントから送られてきたパスワードを比較
    if user and user.validate_password(form.password.data):
      login_user(user, remember=True) # remember=Trueでブラウザを閉じてもログイン状態を保持
      next = request.args.get('next') # ログイン後にリダイレクトするURL
      if not next:
        next = url_for('app.welcome')
      return redirect(next)
  return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm(request.form)
  if request.method == 'POST' and form.validate():
    user = User(
      form.email.data, 
      form.username.data, 
      form.password.data)
    user.add_user()
    return redirect(url_for('app.login'))
  return render_template('register.html', form=form)

@bp.route('/user')
@login_required # ログインしていないとアクセスできない(login_userが実行されていないと)
def user():
  return render_template('user.html')