from flask import Blueprint, render_template

mysite2_bp = Blueprint('mysite2', __name__, template_folder='/site2') # template_folderを指定
# mysite2 = url_for('mysite2/〇〇')で呼び出せるようになる

# http://localhost:5000/mysite2/hello
@mysite2_bp.route('/hello')
def hello():
  return render_template('mysite2/hello.html')