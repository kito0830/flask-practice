from flask import (
    Flask, render_template, request, redirect, url_for, abort, session, flash
)
from wtforms import Form
from wtforms import (
    StringField, IntegerField, BooleanField, DateField, PasswordField,
    RadioField, SelectField, TextAreaField, SubmitField
)
from wtforms.widgets import TextArea
from wtforms.validators import (
    DataRequired, Length, EqualTo, Email, ValidationError, NumberRange
)
from datetime import date

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\x98V\xc9\xd3`\x9f\xf5w;3\xb9\xb0a\xa0@\xb8'

def validate_name2(form, field): # バリデーション自作
    if field.data == 'nanashi2':
        raise ValidationError('その名前も登録できません')

class UserForm(Form):
    name = StringField('名前: ', validators=[validate_name2, DataRequired('データを入力してください')], widget=TextArea(), default='Flask太郎')
    age = IntegerField('年齢: ', validators=[NumberRange(0, 15, message='0~15の範囲で入力して下さい')])
    password = PasswordField('パスワード: ', validators=[Length(1, 16, message='1~16文字で入力して下さい'), EqualTo('confirm_password', message='パスワードが一致しません')])
    birthday = DateField('誕生日: ', format='%Y-%m-%d', render_kw={'placeholder': 'YYYY-mm-dd'})
    gender = RadioField(
        '性別', choices=[('man', '男性'), ('woman', '女性')], default='man'
        )
    major = SelectField('専攻', choices=[('mechanical', '機械工学'), ('electrical', '電気工学'), ('information', '情報工学')])
    is_japanese = BooleanField('日本人ですか？')
    message = TextAreaField('メッセージ: ')
    submit = SubmitField('送信')

    # バリデーションチェック
    def validate_name(self, field):
        if field.data == 'nanashi':
            raise ValidationError('名前が不正です')


# ルートの設定
@app.route('/', methods=['GET','POST'])
def index():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        # sessionにデータを挿入する
        session['name'] = form.name.data
        session['age'] = form.age.data
        session['birthday'] = form.birthday.data
        session['gender'] = form.gender.data
        session['major'] = form.major.data
        session['nationality'] = '日本人' if \
            form.is_japanese.data else '外国人'
        session['message'] = form.message.data
        return redirect(url_for('show_user'))
    
    return render_template('user_regist.html', form=form)

@app.route('/show_user')
def show_user():
    return render_template('show_user.html')



if __name__ == '__main__':
    app.run(debug=True)
