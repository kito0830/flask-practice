from wtforms import Form
from wtforms.fields import (
  HiddenField, StringField, PasswordField, SubmitField, IntegerField, TextAreaField
)

class CreateForm(Form):
  # メンバー情報を作成するフォーム
  name = StringField('名前は：')
  age = IntegerField('年齢は：')
  comment = StringField('コメントは：')
  submit = SubmitField('作成')
  
class UpdateForm(Form):
  # メンバー情報を更新するフォーム
  id = HiddenField('id')
  name = StringField('名前は：')
  age = IntegerField('年齢は：')
  comment = StringField('コメントは：')
  submit = SubmitField('更新')
  
class DeleteForm(Form):
  # メンバー情報を削除するフォーム
  id = HiddenField('id')
  submit = SubmitField('削除')