from flaskr import create_app # flaskr/__init__.pyのcreate_app関数をインポート

app = create_app() # create_app関数を呼び出し、Flaskアプリケーションを生成

if __name__ == '__main__':
  app.run(debug=True) # アプリケーションを起動、debug=Trueでデバッグモードで起動