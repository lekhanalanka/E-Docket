from flask import *
import pyrebase
from functools import wraps
import sys
import os

#new instance of Flask
app = Flask(__name__)

config = {---}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route('/', methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        upload = request.files['upload']
        storage.child("images/educational/PFD.pdf").put(upload)
        return success
    return render_template('files.html')


@app.route('/', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        if request.form['submit'] == 'add':

            qual = request.form['qualification']
            passing = request.form['passing']
            dept = request.form['dept']
            clg = request.form['colg']
            loc = request.form['loc']
            univ = request.form['univ']
            info = request.form['info']


            if(qual=="tenth"):
                db.child("qualifications").child("10th").push(passing)
                db.child("qualifications").child("10th").push(dept)
                db.child("qualifications").child("10th").push(clg)
                db.child("qualifications").child("10th").push(loc)
                db.child("qualifications").child("10th").push(univ)
                db.child("qualifications").child("10th").push(info)
            elif(qual=="twelveth"):
                db.child("qualifications").child("12th").push(passing)
                db.child("qualifications").child("12th").push(dept)
                db.child("qualifications").child("12th").push(clg)
                db.child("qualifications").child("12th").push(loc)
                db.child("qualifications").child("12th").push(univ)
                db.child("qualifications").child("12th").push(info)
            elif(qual=="ug"):
                db.child("qualifications").child("UG").push(passing)
                db.child("qualifications").child("UG").push(dept)
                db.child("qualifications").child("UG").push(clg)
                db.child("qualifications").child("UG").push(loc)
                db.child("qualifications").child("UG").push(univ)
                db.child("qualifications").child("UG").push(info)
            elif(qual=="pg"):
                db.child("qualifications").child("PG").push(passing)
                db.child("qualifications").child("PG").push(dept)
                db.child("qualifications").child("PG").push(clg)
                db.child("qualifications").child("PG").push(loc)
                db.child("qualifications").child("PG").push(univ)
                db.child("qualifications").child("PG").push(info)
            else:
                db.child("qualifications").child("PHD").push(passing)
                db.child("qualifications").child("PHD").push(dept)
                db.child("qualifications").child("PHD").push(clg)
                db.child("qualifications").child("PHD").push(loc)
                db.child("qualifications").child("PHD").push(univ)
                db.child("qualifications").child("PHD").push(info)


            qual = request.form['twelveth']
            passing = request.form['twelveth_passing']
            dept = request.form['twelveth_dept']
            clg = request.form['twelveth_colg']
            loc = request.form['twelveth_loc']
            univ = request.form['twelveth_univ']
            info = request.form['twelveth_info']


            if(qual=="tenth"):
                db.child("qualifications").child("10th").push(passing)
                db.child("qualifications").child("10th").push(dept)
                db.child("qualifications").child("10th").push(clg)
                db.child("qualifications").child("10th").push(loc)
                db.child("qualifications").child("10th").push(univ)
                db.child("qualifications").child("10th").push(info)
            elif(qual=="twelveth"):
                db.child("qualifications").child("12th").push(passing)
                db.child("qualifications").child("12th").push(dept)
                db.child("qualifications").child("12th").push(clg)
                db.child("qualifications").child("12th").push(loc)
                db.child("qualifications").child("12th").push(univ)
                db.child("qualifications").child("12th").push(info)
            elif(qual=="ug"):
                db.child("qualifications").child("UG").push(passing)
                db.child("qualifications").child("UG").push(dept)
                db.child("qualifications").child("UG").push(clg)
                db.child("qualifications").child("UG").push(loc)
                db.child("qualifications").child("UG").push(univ)
                db.child("qualifications").child("UG").push(info)
            elif(qual=="pg"):
                db.child("qualifications").child("PG").push(passing)
                db.child("qualifications").child("PG").push(dept)
                db.child("qualifications").child("PG").push(clg)
                db.child("qualifications").child("PG").push(loc)
                db.child("qualifications").child("PG").push(univ)
                db.child("qualifications").child("PG").push(info)
            else:
                db.child("qualifications").child("PHD").push(passing)
                db.child("qualifications").child("PHD").push(dept)
                db.child("qualifications").child("PHD").push(clg)
                db.child("qualifications").child("PHD").push(loc)
                db.child("qualifications").child("PHD").push(univ)
                db.child("qualifications").child("PHD").push(info)


            qual = request.form['ug']
            passing = request.form['ug_passing']
            dept = request.form['ug_dept']
            clg = request.form['ug_colg']
            loc = request.form['ug_loc']
            univ = request.form['ug_univ']
            info = request.form['ug_info']


            if(qual=="tenth"):
                db.child("qualifications").child("10th").push(passing)
                db.child("qualifications").child("10th").push(dept)
                db.child("qualifications").child("10th").push(clg)
                db.child("qualifications").child("10th").push(loc)
                db.child("qualifications").child("10th").push(univ)
                db.child("qualifications").child("10th").push(info)
            elif(qual=="twelveth"):
                db.child("qualifications").child("12th").push(passing)
                db.child("qualifications").child("12th").push(dept)
                db.child("qualifications").child("12th").push(clg)
                db.child("qualifications").child("12th").push(loc)
                db.child("qualifications").child("12th").push(univ)
                db.child("qualifications").child("12th").push(info)
            elif(qual=="ug"):
                db.child("qualifications").child("UG").push(passing)
                db.child("qualifications").child("UG").push(dept)
                db.child("qualifications").child("UG").push(clg)
                db.child("qualifications").child("UG").push(loc)
                db.child("qualifications").child("UG").push(univ)
                db.child("qualifications").child("UG").push(info)
            elif(qual=="pg"):
                db.child("qualifications").child("PG").push(passing)
                db.child("qualifications").child("PG").push(dept)
                db.child("qualifications").child("PG").push(clg)
                db.child("qualifications").child("PG").push(loc)
                db.child("qualifications").child("PG").push(univ)
                db.child("qualifications").child("PG").push(info)
            else:
                db.child("qualifications").child("PHD").push(passing)
                db.child("qualifications").child("PHD").push(dept)
                db.child("qualifications").child("PHD").push(clg)
                db.child("qualifications").child("PHD").push(loc)
                db.child("qualifications").child("PHD").push(univ)
                db.child("qualifications").child("PHD").push(info)

            qual = request.form['pg']
            passing = request.form['pg_passing']
            dept = request.form['pg_dept']
            clg = request.form['pg_colg']
            loc = request.form['pg_loc']
            univ = request.form['pg_univ']
            info = request.form['pg_info']


            if(qual=="tenth"):
                db.child("qualifications").child("10th").push(passing)
                db.child("qualifications").child("10th").push(dept)
                db.child("qualifications").child("10th").push(clg)
                db.child("qualifications").child("10th").push(loc)
                db.child("qualifications").child("10th").push(univ)
                db.child("qualifications").child("10th").push(info)
            elif(qual=="twelveth"):
                db.child("qualifications").child("12th").push(passing)
                db.child("qualifications").child("12th").push(dept)
                db.child("qualifications").child("12th").push(clg)
                db.child("qualifications").child("12th").push(loc)
                db.child("qualifications").child("12th").push(univ)
                db.child("qualifications").child("12th").push(info)
            elif(qual=="ug"):
                db.child("qualifications").child("UG").push(passing)
                db.child("qualifications").child("UG").push(dept)
                db.child("qualifications").child("UG").push(clg)
                db.child("qualifications").child("UG").push(loc)
                db.child("qualifications").child("UG").push(univ)
                db.child("qualifications").child("UG").push(info)
            elif(qual=="pg"):
                db.child("qualifications").child("PG").push(passing)
                db.child("qualifications").child("PG").push(dept)
                db.child("qualifications").child("PG").push(clg)
                db.child("qualifications").child("PG").push(loc)
                db.child("qualifications").child("PG").push(univ)
                db.child("qualifications").child("PG").push(info)
            else:
                db.child("qualifications").child("PHD").push(passing)
                db.child("qualifications").child("PHD").push(dept)
                db.child("qualifications").child("PHD").push(clg)
                db.child("qualifications").child("PHD").push(loc)
                db.child("qualifications").child("PHD").push(univ)
                db.child("qualifications").child("PHD").push(info)


            qual = request.form['phd']
            passing = request.form['phd_passing']
            dept = request.form['phd_dept']
            clg = request.form['phd_colg']
            loc = request.form['phd_loc']
            univ = request.form['phd_univ']
            info = request.form['phd_info']


            if(qual=="tenth"):
                db.child("qualifications").child("10th").push(passing)
                db.child("qualifications").child("10th").push(dept)
                db.child("qualifications").child("10th").push(clg)
                db.child("qualifications").child("10th").push(loc)
                db.child("qualifications").child("10th").push(univ)
                db.child("qualifications").child("10th").push(info)
            elif(qual=="twelveth"):
                db.child("qualifications").child("12th").push(passing)
                db.child("qualifications").child("12th").push(dept)
                db.child("qualifications").child("12th").push(clg)
                db.child("qualifications").child("12th").push(loc)
                db.child("qualifications").child("12th").push(univ)
                db.child("qualifications").child("12th").push(info)
            elif(qual=="ug"):
                db.child("qualifications").child("UG").push(passing)
                db.child("qualifications").child("UG").push(dept)
                db.child("qualifications").child("UG").push(clg)
                db.child("qualifications").child("UG").push(loc)
                db.child("qualifications").child("UG").push(univ)
                db.child("qualifications").child("UG").push(info)
            elif(qual=="pg"):
                db.child("qualifications").child("PG").push(passing)
                db.child("qualifications").child("PG").push(dept)
                db.child("qualifications").child("PG").push(clg)
                db.child("qualifications").child("PG").push(loc)
                db.child("qualifications").child("PG").push(univ)
                db.child("qualifications").child("PG").push(info)
            else:
                db.child("qualifications").child("PHD").push(passing)
                db.child("qualifications").child("PHD").push(dept)
                db.child("qualifications").child("PHD").push(clg)
                db.child("qualifications").child("PHD").push(loc)
                db.child("qualifications").child("PHD").push(univ) 
                db.child("qualifications").child("PHD").push(info)
        return render_template('qualification.html')

if __name__=='__main__':
    app.run(debug=true)
                
