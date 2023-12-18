## Pythonの仮想環境構築
```
virtualenv myenv
```

### 仮想間環境をインストールする（virtualenv）
```
pip install virtualenv
```

### 仮想環境のアクティベート
```
myenv\Scripts\activate
```

### 仮想環境内での作業
```
pip install ライブラリ名
```

### 仮想環境の終了
```
deactivate
```



## Flaskの環境構築
### 仮想環境の構築
```
virtualenv flaskenv
```
### 仮想環境のアクティベート
Winの場合
```
flaskenv\Scripts\activate
```

MAcの場合
```
. flaskenv/bin/activate
```

### flaskをインストール
```
pip install flask
```

### ルートディレクトリにapp.pyを作成
```
from flask import Flask

# ルートの設定と立ち上げ処理の設定に使用する変数
app = Flask(__name__) 


# ルートの設定
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__': # このファイルが実行された時に以下の処理を実行する
    app.run() # 上記で定義したappを起点にFlaskを立ち上げる
```


### 環境変数の設定
```
set FLASK_APP=app.py
```

### Flaskの実行
```
python app.py
```

### データベースとの接続
・sql-alchemyをインストール
```
pip install flask-sqlalchemy
```

・migrateをインストール
```
pip install flask-migrate  
```

・migrateの実行準備（マイグレートファイルの設定）
```
export FLASK_APP=migrate_model.py
```

```
flask db init
```

→migrationsフォルダが作成される

・マイグレーションファイルを作成
```
flask db migrate -m "add Person"
```

マイグレーションを実行
```
flask db upgrade
```

