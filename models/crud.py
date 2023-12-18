from model import db, Person, app

with app.app_context():
  db.create_all() # テーブルを作成

# データを追加
man1 = Person("Taro", 18)
man2 = Person("Jiro", 21)
man3 = Person("Saburo", 25)

print(man1)
print(man2)
print(man3)

with app.app_context():
  db.session.add_all([man1, man2]) # 複数データを追加
  db.session.add(man3) # 単数データを追加

  db.session.commit() # データを保存
  print(man1, man2, man3)