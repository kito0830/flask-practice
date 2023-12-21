from models import db, Person, app
from datetime import datetime

man1 = Person('Taro', "090-1111-1115", 21, datetime.now(), datetime.now())
man2 = Person('Jiro', "090-1111-1113", 21, datetime.now(), datetime.now())
man3 = Person('Saburo', "090-1111-1114", 21, datetime.now(), datetime.now())

# データを追加
with app.app_context(): # withブロック内でデータベースにアクセス
  # db.session.add_all([man1, man2, man3]) # 複数データを追加
  # db.session.commit() # データを保存
  
  print(Person.query.get(3)) # id=1のデータを取得
  
  # for x in Person.query.all():
  #   print(x.name)
    
  # for x in Person.query.filter_by(name='Taro'):
  #   print(x.name)
  
  # id 1 を削除
  # Person.query.filter_by(id=1).delete()
  # db.session.commit()
  
  
  Person.query.filter_by(name='nanashi').update({
    'name': 'John',
    'update_at' : datetime.now()
    })
  db.session.commit()