from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Alexander'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user,
                           )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


'''
UPD 1:
можно разместить код html и тут (ниже), но мы рендерим шаблон с файла index.html
  <body>
    <h1>a = ''' '+ str(a) +' '''<h1>
    <form action=add1 method=post>
    <dd><input type=submit value=Yes>
    </dl>
    </form>
    <button onclick="add1()" type="button">перейти</button>
  </body>
'''
