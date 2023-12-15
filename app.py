from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, IntegerField, validators
from wtforms.form import Form

# ルートの設定と立ち上げ処理の設定に使用する変数
app = Flask(__name__)

# SECRET_KEYは
# import os
# print(os.urandom(16))で作成
app.config['SECRET_KEY'] = b'\x98V\xc9\xd3`\x9f\xf5w;3\xb9\xb0a\xa0@\xb8' 

class UserForm(Form) : # wtformsのFormクラスを継承
    name = StringField('名前')
    age = IntegerField('年齢')
    submit = SubmitField('送信')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = age = ''
    form = UserForm(request.form) # formオブジェクトを作成

    # フォームの作成
    if request.method == 'POST':

        # バリデーションチェック
        if form.validate(): # バリデーションチェックに問題がない場合
            name = form.name.data # フォームの入力値を取得
            age = form.age.data # フォームの入力値を取得
            form = UserForm() # index.htmlに返すフォームを初期化する
        else:
            print('入力内容に問題があります')

    return render_template('index.html', name=name, age=age, form=form)


if __name__ == '__main__': # このファイルが実行された時に以下の処理を実行する
    app.run(debug=True) # 上記で定義したappを起点にFlaskを立ち上げる
