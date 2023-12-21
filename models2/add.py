from models import db, Person, app
from datetime import datetime

man1 = Person(None, "090-1111-1112", 21, datetime.now(), datetime.now())

with app.app_context():
  db.session.add(man1)
  db.session.commit()