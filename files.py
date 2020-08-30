from flask import *
import pyrebase
from functools import wraps
import sys
import os

#new instance of Flask
app = Flask(__name__)

config = {-----}


#init firebase
firebase = pyrebase.initialize_app(config)
#real time database instance
storage = firebase.storage()


@app.route('/', methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        tenth = request.files['tenth']
        twelveth = request.files['twelveth']
        ug = request.files['ug']
        pg = request.files['pg']
        phd = request.files['phd']
        storage.child("Educational/tenth.pdf").put(tenth)
        storage.child("Educational/twelveth.pdf").put(twelveth)
        storage.child("Educational/ug.pdf").put(ug)
        storage.child("Educational/pg.pdf").put(pg)
        storage.child("Educational/phd.pdf").put(phd)
        return 'success'
    return render_template('file_upload.html')
