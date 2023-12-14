from flask import Flask

# ルートの設定と立ち上げ処理の設定に使用する変数
app = Flask(__name__) 

# ルートの設定
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello')
def hellow():
    # /helloにアクセスした時 
    return '<h1>Hello</h1>'

posts = {
    1: 'POST1',
    2: 'POST2',
}

@app.route('/post/<int:post_id>/<post_name>')
def show_post(post_id, post_name):
    # /post/<post_id>にアクセスした時 
    return f"{post_id} : {post_name}"


@app.route('/user/<username>/<int:user_number>')
def show_user(username, user_number):
    user_name_number =f"{username} : {user_number}"
    return f'<h1>{user_name_number}</h1>'

if __name__ == '__main__': # このファイルが実行された時に以下の処理を実行する
    app.run(debug=True) # 上記で定義したappを起点にFlaskを立ち上げる
