from flask import Flask, render_template, redirect, url_for, abort
from datetime import datetime

# ルートの設定と立ち上げ処理の設定に使用する変数
app = Flask(__name__) 

@app.template_filter('reverse_name')
def reverse(name):
    return name[-1::-1] # 文字列を逆順にする

@app.template_filter('born_year')
def calcurate_born_year(age):
    now_timestamp = datetime.now()
    return str(now_timestamp.year - age) + '年'

# ルートの設定
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/<string:user_name>/<int:age>')
def home(user_name, age):
    login_user =  {
        'name': user_name,
        'age': age
    }
    return render_template('home.html', user_info=login_user)

class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/user_list')
def user_list():
    # users = [
    #    'Taro','Suzuki','Yamada','Sato','Watanabe', 'Tanaka'
    # ]
    users = [
        UserInfo('Taro', 20),
        UserInfo('Suzuki', 30),
        UserInfo('Yamada', 40),
        UserInfo('Sato', 50),
        UserInfo('Watanabe', 60),
    ]
    is_login = False
    return render_template('user_list.html', users=users , is_login=is_login)

@app.route('/user/<string:user_name>/<int:age>')
def user(user_name, age):
    if user_name in ['Taro', 'Jiro', 'Saburo']:
        return redirect(url_for('home', user_name=user_name, age=age))
    else:
        abort(500, 'そのユーザーはリダイレクトできません')

@app.errorhandler(500)
def system_error(error):
    error_description = error.description
    return render_template('system_error.html', error_description=error_description), 500


@app.errorhandler(404)
# 404エラー
def page_not_found(error):
    return render_template('not_found.html'), 404


if __name__ == '__main__': # このファイルが実行された時に以下の処理を実行する
    app.run(debug=True) # 上記で定義したappを起点にFlaskを立ち上げる
