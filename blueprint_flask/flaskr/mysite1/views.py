from flask import Blueprint, render_template

mysite1_bp = Blueprint('mysite1', __name__, template_folder='/site1') # template_folderを指定

# http://localhost:5000/mysite1/hello
@mysite1_bp.route('/hello')
def hello():
  return render_template('mysite1/hello.html')