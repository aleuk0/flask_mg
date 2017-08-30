'''
UPD: не понадобилось
__init__.py is imported using a directory. if you want to import it as app you
should put __init__.py file in directory named app
a better option is just to rename __init__.py to app.py
'''


from flask import Flask

app = Flask(__name__)

from app import views
'''
UPD: не понадобилось
There is no need to import the views in your project-level file. You are not
using them there, so no reason to import them.
If you did need to, you would just to from blog import views, because the views
are in the blog directory and manage.py puts the top-level directory into the
Python path.
'''
