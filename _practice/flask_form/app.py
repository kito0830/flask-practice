from flask import Flask, render_template, redirect, url_for, abort, request
from werkzeug.utils import secure_filename
import pykakasi
import os

app = Flask(__name__)

class Kakashi:
    kakashi = pykakasi.kakasi()
    kakashi.setMode('H', 'a') # ひらがなをasciiに置き換える
    kakashi.setMode('K', 'a') # カタカナをasciiに置き換える
    kakashi.setMode('J', 'a') # 漢字をasciiに置き換える
    conv = kakashi.getConverter()

    @classmethod
    def japanese_to_ascii(cls, japanese): # ひらがな・カタカナ・漢字をasciiに置き換える
        return cls.conv.do(japanese) 


class UserInfo:
    def __init__(self, last_name, first_name, gender, job, message):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.job = job
        self.message = message


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    print(request.full_path)
    print(request.method)
    print(request.args)
    
    # GET通信の場合(args)
    # user_info = UserInfo(
    #     request.args.get('last_name'),
    #     request.args.get('first_name'),
    #     request.args.get('gender'),
    #     request.args.get('job'),
    #     request.args.get('message')
    # )

    # POST通信の場合(form)
    user_info = UserInfo(
        request.form.get('last_name'),
        request.form.get('first_name'),
        request.form.get('gender'),
        request.form.get('job'),
        request.form.get('message')
    )
    return render_template('home.html', user_info=user_info)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        file = request.files['file']
        ascii_filename = Kakashi.japanese_to_ascii(file.filename) # ひらがな・カタカナ・漢字をasciiに置き換える
        save_filename = secure_filename(ascii_filename) # ./等の危険な文字列を削除してくれる
        file.save(os.path.join('./static/image', save_filename)) # ファイルを保存する

        return redirect(url_for('uploaded_file', filename=save_filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)



if __name__ == '__main__': # このファイルが実行された時に以下の処理を実行する
    app.run(debug=True) # 上記で定義したappを起点にFlaskを立ち上げｃｃ
