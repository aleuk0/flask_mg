from flask import render_template
from app import app

a = 1

@app.route('/')
@app.route('/index')
def index():
    global a
    user = {'nickname': 'Alexander'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user,
                           a = a)
'''
можно разместить все тут(ниже), но мы рендерим шаблон с файла index.html
  <body>
    <h1>a = ''' + str(a) + '''<h1>
    <form action=add1 method=post>
    <dd><input type=submit value=Yes>
    </dl>
    </form>
    <button onclick="add1()" type="button">перейти</button>
  </body>
'''

@app.route('/yes', methods=['POST'])
def yes():
    global a
    a += 1
    user = {'nickname': 'Alexander'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user,
                           a = a)
