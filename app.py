import os
import datetime
import pyqrcode
from io import BytesIO
from werkzeug.utils import secure_filename

from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
from database import db_connect, storedata, vlicences, vlicence,reg,user_login,storercdata,vrc,vrc1,admin_login,users


app = Flask(__name__)
app.secret_key = os.urandom(24)
UPLOAD_FOLDER = 'C:\\Users\\dell\\Documents\\Python\\QR code\\static\\UploadImages'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def FUN_root():
    return render_template("index.html")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/enterdatap")
def enterdatap():
    return render_template("enterdata.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/vuser")
def vuser():
    data = users()
    return render_template("vuser.html",user=data)

@app.route("/adminhome")
def vrc4():
    return render_template("adminhome.html")
#--------------------------------------------------Register----------------------------------------------------------------------#
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        status = reg(request.form['username'],request.form['password'],request.form['dob'],request.form['email'],request.form['address'],request.form['mobile'])
        if status == 1:
            return render_template("user.html", m1="sucess")
        else:
            return render_template("register.html", m2="Failed")

#===================================================Login==============================================================================
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        status = user_login(request.form['username'],request.form['password'])
        if status == 1:
            return render_template("enterdata.html", m1="sucess")
        else:
            return render_template("user.html", m2="Failed")

@app.route("/adminlogin", methods=['GET', 'POST'])
def alogin():
    if request.method == 'POST':
        status = admin_login(request.form['username'],request.form['password'])
        if status == 1:
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m2="Failed")

@app.route("/licence", methods = ['GET','POST'])
def licence():
    id=request.args.get('id')
    data3 = vlicence(id)
    session['id'] = id
    # data = qrcode(data3)
    # print(data)
    return render_template("licence.html",userdata=data3)

@app.route("/licences")
def licences():
    data = vlicences()
    return render_template("vlicences.html",userdata=data)  

@app.route("/rc", methods = ['GET','POST'])
def rcdata2():
    id=request.args.get('id')
    data3 = vrc(id)
    session['id'] = id
    # data = qrcode(data3)
    # print(data)
    return render_template("rc.html",rcsdata=data3)

@app.route("/vrc")
def rcdata1():
    data = vrc1()
    return render_template("vrc.html",rcsdata=data)    

@app.route("/qrcode",methods = ['GET','POST'])
def qrcode():
    # id=request.args.get('id')
    id = session['id']
    data3 = vlicence(id)
    data = "Name: "+str(data3[0][1]) +"\n"+"Father's Name: "+ data3[0][2] +"\n"+"Date Of Birth: "+ data3[0][3] +"\n"+"House No: "+ data3[0][4] +"\n"+"Colony: "+ data3[0][5] +"\n"+"Location: "+ data3[0][6] +"\n"+"Mandal: "+ data3[0][7] +"\n"+"District: "+ data3[0][8] +"\n"+"Pin: "+ data3[0][9] +"\n"+"Date Of Issue: "+ data3[0][10] +"\n"+"Validity: "+ data3[0][11]
    url = pyqrcode.create(data)
    stream = BytesIO()
    url.svg(stream, scale=3)
    return stream.getvalue(), 200, {
        'Content-Type': 'image/svg+xml',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}


@app.route("/qrcode1",methods = ['GET','POST'])
def qrcode1():
    # id=request.args.get('id')
    id = session['id']
    data3 = vrc(id)
    data = "reg.No: "+str(data3[0][1]) +"\n"+"Regd.Owner: "+ data3[0][2] +"\n"+"Address: "+ data3[0][3] +"\n"+"Maker's Class: "+ data3[0][4] +"\n"+"Vehicle Class: "+ data3[0][5] +"\n"+"Yr. of Mfg: "+ data3[0][6] +"\n"+"Fuel Used: "+ data3[0][7] +"\n"+"Type Of Body: "+ data3[0][8] +"\n"+"Chassis No: "+ data3[0][9] +"\n"+"Engine No: "+ data3[0][10] +"\n"+"CC: "+ data3[0][11]
    url = pyqrcode.create(data)
    stream = BytesIO()
    url.svg(stream, scale=3)
    return stream.getvalue(), 200, {
        'Content-Type': 'image/svg+xml',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}



# ------------------Add Data----------------------------
@app.route("/enterdata", methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        f = request.files['photo']
        g = request.files['usersign']
        h = request.files['authoritysign']
        photoname=secure_filename(f.filename)
        signname=secure_filename(g.filename)
        asignname=secure_filename(h.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))
        g.save(os.path.join(app.config['UPLOAD_FOLDER'], signname))
        h.save(os.path.join(app.config['UPLOAD_FOLDER'], asignname))
        status = storedata(request.form['name'], request.form['fname'],request.form['dob'],request.form['hno'],request.form['colony'],request.form['location'],request.form['mandal'],request.form['dist'],request.form['pin'],request.form['rta'],photoname,signname,asignname,request.form['ref'],request.form['vtype'],request.form['badge'],request.form['blood'])
        if status == 1:
            return render_template("enterdata.html", m1="sucess")
        else:
            return render_template("enterdata.html", m2="Failed")
    else:
        return render_template("enterdata.html")

@app.route("/rcdata", methods=['GET', 'POST'])
def srcdata():
    if request.method == 'POST':
        f = request.files['osign']
        g = request.files['authoritysign']
        
        photoname=secure_filename(f.filename)
        signname=secure_filename(g.filename)
        
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], photoname))
        g.save(os.path.join(app.config['UPLOAD_FOLDER'], signname))
        
        status = storercdata(request.form['regnum'], request.form['regowner'],request.form['address'],request.form['mclass'],request.form['vclass'],request.form['mfgdate'],request.form['fused'],request.form['bodytype'],request.form['cnumber'],request.form['enumber'],request.form['cc'],request.form['wbaase'],request.form['scapacity'],request.form['uweight'],request.form['color'],request.form['tax'],request.form['hto'],photoname,signname)
        if status == 1:
            return render_template("rcdata.html", m1="sucess")
        else:
            return render_template("rcdata.html", m2="Failed")
    else:
        return render_template("enterdata.html")



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
